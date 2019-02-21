import time

def compare_time(regiment):
    #This function compares the date in medication regiments with the current time, if they are the same, then returns
    #'Y', else returns 'N'.
    time1 = time.localtime()
    keys = list(regiment.keys())
    year = keys[0][0:4]
    month = keys [0][7]
    date = keys[0][7:9]
    hour = keys[0][10:12]
    if str(time1.tm_year) == year and str(time1.tm_mon)== month and str(time1.tm_mday) == date and str(time1.tm_hour) == hour:
        return 'Y'
    else:
        return 'N'

# Test case for compare_time function
# reg_info = {'2019 2 20 19':'00', '2019 2 20 19':'00'}
# compare_time(reg_info)

