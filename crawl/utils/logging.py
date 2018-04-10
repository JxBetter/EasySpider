import time


def log(*args,**kwargs):
    print(time.strftime('***%y-%m-%d---%H:%M:%S***'),*args,**kwargs)