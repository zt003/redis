import time
import datetime
import json

def compare_time(regiment):
    #This function compares the date in medication regiments with the current time, if they are the same, then returns
    #'Y', else returns 'N'.
    time1 = time.localtime()
    keys = list(regiment.keys())
    year = keys[0][0:4]
    month = keys [0][7]
    date = keys[0][7:9]
    hour = keys[0][10:11]
    print(hour)
    if str(time1.tm_year) == year and str(time1.tm_mon)== month and str(time1.tm_mday) == date and str(time1.tm_hour) == hour:
        return 1
    else:
        return 0

def validate(year,mon,day,hour,min):
    #validate if time is early or late
    past = datetime.date(year,mon,day)
    x = datetime.datetime.now()
    present = datetime.date(x.year,x.month,x.day)
    if past < present:
        #print('early1')
        return 'N'
    elif past > present:
        #print('late2')
        return 'Y'
    else:
        regimen = datetime.datetime(year, mon, day, hour, min, 1, 1)
        if x.time() < regimen.time():
            #print('late1')
            return 'Y'
        else:
            #print('early2')
            return 'N'


# Test case for compare_time function
# Y means valid
# N means invalid
# reg_info = {'2019 2 20 19':'00', '2019 2 20 19':'00'}
# compare_time(reg_info)
#x= validate(2019,2,24,22,5)
#x = compare_datetime(2019,3,4,14,5)
#print(x)
