import redis
import time
import queue
from help import *
from motor import *




reg_info = {'2019 2 21 0':'00', '2019 2 20 19':'00'} #Medication Regiments
Re_Button_Pressed = 0 #Release Button Pressed Flg
Sleep_Button_Pressed = 1 #Sleep Button Pressed Flag
Release_Count = 0 #Time that the user pressed the sleep button
temp_time = 0 #time register
right_time = 'N' #Is it the right time to dispense?
release = 0 #Time to release flag
non_adherence = 0 #Non adherence system flag
listen = 1

dispense_motor = Motor('dispense motor',2000,100) #Dispensing Motor Object
cut_motor = Motor('cutting motor',3000,100) #Cutting Motor Object
nonad_motor = Motor('non_ad motor',4000,100) #Non-Adherence Motor Object
data_logger = dict() #Initialize a data logger

redisClient = redis.Redis()
redisPublisher = redis.Redis()

pubsub = redisClient.pubsub()
pubsub.subscribe("Interface","wireless")


for item in pubsub.listen():
    if type(item['data']) is not int:
        item = str(item['data'],'utf-8')
        print('Medication Regimen Received')
        print(item)
        print('')
        break

def main():

    global Re_Button_Pressed
    global Sleep_Button_Pressed
    global Release_Count
    global temp_time
    global release
    global right_time
    global non_adherence
    global listen


    #right_time = compare_time(reg_info)
    right_time = 'Y'
    if right_time == 'Y': # If it is time to dispense medication
        release = 1  #set the release flag to yes
        #send information interface, notify the user
    cur_time = (time.time())//60
    if cur_time - temp_time == 30: #30 min after pressing sleep button
        release = 1 #set the release flag to yes
        #send information to interface module, notify the user


    if release == 1:
        for item in pubsub.listen():
            if item['data'] == b'Release-yes':
                print("User pressed the release button")
                print('')
                Re_Button_Pressed = 1
                break
            elif item['data'] == b'Release-no':
                print('User does not pressed the release button')
                print('')
                break

        if Re_Button_Pressed == 0:
            for item in pubsub.listen():
                if item['data'] == b'Nonad-yes':
                    non_adherence = 1
                    break
                elif item['data'] == b'Nonad-no':
                    Re_Button_Pressed = 1
                    break
                elif item['data'] == b'Sleep-yes':
                    release = 0
                    break

        if Re_Button_Pressed == 1:
            #print('1')
            print("Pill is dispensing")
            dispense_motor.Forward()
            cut_motor.Forward()
            data_logger[str(str(time.asctime()))] = 'adhere'
            redisPublisher.publish("This is main","Medrun")
            print('')
            non_adherence = 0
            Re_Button_Pressed = 0

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
            #print('2')
            print('Activate the non-adherence mechanism')
            nonad_motor.Forward()
            dispense_motor.Forward()
            cut_motor.Forward()
            data_logger[str(str(time.asctime()))] = 'not adhere'
            redisPublisher.publish("This is main","Nonad-run")
            print('')
            non_adherence = 0
            Re_Button_Pressed = 0

                    #send information to motor system (Keith)
                    #send information to motor system (Garrett)



while True:
    main()