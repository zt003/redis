import redis
import time
import queue
from time-test import*

reg_info = {'2019 2 20 19':'00', '2019 2 20 19':'00'}
Re_Button_Pressed = 0
Sleep_Button_Pressed = 0
Release_Count = 0

compare_time(reg_info)

def main():

    global Re_Button_Pressed
    global Sleep_Button_Pressed
    global Release_Count
    if Med_reg['data'] == 'good':
        #send information interface, notify the user
        localtime = time.asctime(time.localtime(time.time()))  #Time looks like this:Tue Jan 13 10:17:09 2009"
        if Re_Button_Pressed == 1:
            #send information to motor system (Garret)
        if Sleep_Button_Pressed ==  1:
            if Release_Count <= 5:
                Release_Count += 1
            elif Release_Count == 6:
                #send information to motor system (Keith)
                #send information to motor system (Garrett)



