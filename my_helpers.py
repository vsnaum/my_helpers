import pickle
import datetime
import pytz


def pkl_dump(filename,obj):
    with open(filename,'wb') as f:
        pickle.dump(obj,f)

def pkl_load(filename):
    with open(filename,'rb') as f:
        obj = pickle.load(f)
    return obj

def curr_time(tz='Europe/Moscow'):
    tz = pytz.timezone(tz)
    dt = datetime.datetime.now(tz)
    dt = dt.strftime("%Y-%m-%d_%H-%M-%S")
    return dt
