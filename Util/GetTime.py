import time

def get_current_date():
    year = time.localtime().tm_year
    month = time.localtime().tm_mon
    day = time.localtime().tm_mday
    return "%s-%s-%s" % (year,month,day)

def get_current_time():
    hour = time.localtime().tm_hour
    min = time.localtime().tm_min
    sec = time.localtime().tm_sec
    return "%s时%s分%s秒" % (hour, min, sec)

def get_current_time1():
    hour = time.localtime().tm_hour
    min = time.localtime().tm_min
    sec = time.localtime().tm_sec
    return "%s:%s:%s" % (hour, min, sec)