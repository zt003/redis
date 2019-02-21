import redis
import time
import queue
from help import *
from motor import *




reg_info = {'2019 2 20 23':'00', '2019 2 20 19':'00'} #Medication Regiments
Re_Button_Pressed = 0 #Release Button Pressed Flg
Sleep_Button_Pressed = 1 #Sleep Button Pressed Flag
Release_Count = 0 #Time that the user pressed the sleep button
temp_time = 0 #time register
right_time = 'N' #Is it the right time to dispense?
release = 0 #Time to release flag
non_adherence = 0 #Non adherence system flag

dispense_motor = Motor('dispense motor',2000,100) #Dispensing Motor Object
cut_motor = Motor('cutting motor',3000,100) #Cutting Motor Object
nonad_motor = Motor('non_ad motor',4000,100) #Non-Adherence Motor Object
data_logger = dict() #Initialize a data logger

redisClient = redis.Redis()
redisPublisher = redis.Redis()

pubsub = redisClient.pubsub()
pubsub.subscribe("Button Pressed")


def main():

    global Re_Button_Pressed
    global Sleep_Button_Pressed
    global Release_Count
    global temp_time
    global release
    global right_time
    global non_adherence

    right_time = compare_time(reg_info)
    if right_time == 'Y': # If it is time to dispense medication
        release = 1  #set the release flag to yes
        #send information interface, notify the user
    cur_time = (time.time())//60
    if cur_time - temp_time == 30: #30 min after pressing sleep button
        release = 1 #set the release flag to yes
        #send information to interface module, notify the user

    if release == 1:
        for item in pubsub.listen():
            listen_time = time.time()//60
            if item['data'] == b'yes':
                print("User pressed the button")
                Re_Button_Pressed = 1
                break
            if cur_time - listen_time == 30:
                print('non')
                non_adherence = 1
                break
        if Re_Button_Pressed == 1:
            dispense_motor.Forward()
            cut_motor.Forward()
            data_logger[str(str(time.asctime()))] = 'adhere'
        if Sleep_Button_Pressed == 1:
            if Release_Count <= 5:
                # enter the sleep mode
                Release_Count += 1
                temp_time = (time.time()) // 60
            elif Release_Count == 6:
                #turn on the non-adherence system
                non_adherence = 1
        if non_adherence == 1:
            nonad_motor.Forward()
            dispense_motor.Forward()
            data_logger[str(str(time.asctime()))] = 'not adhere'
            non_adherence = 0

                    #send information to motor system (Keith)
                    #send information to motor system (Garrett)



while True:
    main()