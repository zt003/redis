import redis
import time
import queue
import datetime
from help import *
from motor import *



reg = [] #medication regiment holder
Re_Button_Pressed = 0 #Release Button Pressed Flg
Sleep_Button_Pressed = 0 #Sleep Button Pressed Flag
Snooze_Count = 0 #Time that the user pressed the sleep button
temp_time = 0 #time register for snoozing
outer_time = 0 #time register for the overall period
right_time = 'N' #Is it the right time to dispense?
release = 0 #Time to release flag
non_adherence = 0 #Non adherence system flag
invalid_counter = 0 #This counter keeps track of how many invalid regimen is there

dispense_motor = Motor('dispense motor',2000,100) #Dispensing Motor Object
cut_motor = Motor('cutting motor',3000,100) #Cutting Motor Object
nonad_motor = Motor('non_ad motor',4000,100) #Non-Adherence Motor Object
data_logger = dict() #Initialize a data logger

redisClient = redis.Redis()
redisPublisher = redis.Redis()

pubsub = redisClient.pubsub()
pubsub.subscribe("Interface","wireless")


def main():

    global Re_Button_Pressed
    global Sleep_Button_Pressed
    global Snooze_Count
    global temp_time
    global release
    global right_time
    global non_adherence
    global reg
    global invalid_counter
    global outer_time

    if len(reg) == 0:
        redisPublisher.publish("This is main","yes")

    for item in pubsub.listen():
        # These lines here ensure that the regimen main file received from Wireless module is valid
        if type(item['data']) is not int:
            item = str(item['data'], 'utf-8')
            reg = item.split()
            print('Medication Regimen Received')
            if validate(int(reg[0]), int(reg[1]), int(reg[2]), int(reg[3]), int(reg[4])) == 'N':
                print('Medication Regimen is invalid')
                invalid_counter += 1
                redisPublisher.publish("This is main", "invalid")
            else:
                print('Medication Regimen is valid')
                redisPublisher.publish("This is main", "valid")
                break

    while invalid_counter > 0:
        #These lines storages all the missed medication into the storage space
        print('Activate the non-adherence mechanism for invalid medication')
        nonad_motor.Forward()
        dispense_motor.Forward()
        cut_motor.Forward()
        invalid_counter -= 1

    # These lines Test if it is the right time to take medication, if so, change the flag to 1, go to state 5
    # if compare_time(reg) == 1:
    #     release = 1


    if release == 1:
        outer_time = (time.time())//60
        #Alarm the User
        #Now it is in state 5
        if Re_Button_Pressed == 1:
            # If the user pressed the release button, release medication and go to state 6
            print('Release Button Pressed')
            print("Pill is dispensing")
            dispense_motor.Forward()
            cut_motor.Forward()
            data_logger[str(str(time.asctime()))] = 'adhere'
            redisPublisher.publish("This is main","Medrun")
            print('')
            non_adherence = 0
            Re_Button_Pressed = 0
            release = 0 # Set the release flag back to 0
            reg = []

        elif Sleep_Button_Pressed == 1:
            #If the user pressed the snooze button, go to state 7 and snooze
            if Snooze_Count <=5:
                #In state 7, the machine will sleep for 30 min unless release button is pressed or time is up
                Snooze_Count += 1
                print('Snooze Button Pressed')
                temp_time = (time.time())//60
                cur_time = (time.time())//60
                while cur_time - temp_time < 30: #This while loop handles the case when the machine is snoozing, the snoozing will stop if it reaches 30min of the user pressed the Release Button.
                    cur_time = (time.time())/60
                    if Re_Button_Pressed == 1: #If the user pressed the release button,break out of the sleep session
                        break
            elif Snooze_Count > 5:
                non_adherence = 1
                release = 0

        # if Sleep_Button_Pressed == 1:
        #     print('1')
        #     if Release_Count <= 5:
        #         # enter the sleep mode
        #         Release_Count += 1
        #         temp_time = (time.time()) // 60
        #     elif Release_Count == 6:
        #         #turn on the non-adherence system
        #         non_adherence = 1

        if non_adherence == 1:
            #If the non adherence flag is turned on,store the medication in the non-adherence storage space
            print('Activate the non-adherence mechanism')
            nonad_motor.Forward()
            dispense_motor.Forward()
            cut_motor.Forward()
            data_logger[str(str(time.asctime()))] = 'not adhere' #store the data logger in the dictionary
            redisPublisher.publish("This is main","Nonad-run") #send the non-adherence data
            non_adherence = 0  #Reset the non adherence flag
            Re_Button_Pressed = 0 #Reset the Button Pressed flag
            reg = [] #Clear the regimen

                    #send information to motor system (Keith)
                    #send information to motor system (Garrett)



while True:
    main()
