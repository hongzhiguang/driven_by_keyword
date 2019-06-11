import os
import os.path
import time
from Util.Log import *

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

def make_date_dir(dir_path):
    if os.path.exists(dir_path):
        cur_date = get_current_date()
        path = os.path.join(dir_path,cur_date)
        if not os.path.exists(path):
            os.mkdir(path)
            return path
        else:
            logging.info("%s already exist!" % path)
            return path
    else:
        logging.info("%s does not exist!" % dir_path)

def make_time_dir(dir_path):
    if os.path.exists(dir_path):
        cur_time = get_current_time()
        path =os.path.join(dir_path,cur_time)
        if not os.path.exists(path):
            os.mkdir(path)
            return path
        else:
            logging.info("%s already exist!" % path)
            return path
    else:
        logging.info("%s does not exist!" % dir_path)