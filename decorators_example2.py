# Performance of function using deccorator
# import time from time
from time import time


def performance(func):
    def wrapper(*args, **kargs):
        t1 = time()
        result = func(*args, **kargs)
        t2 = time()
        print(f"Time Used: {t2-t1}")
        return result
    return wrapper


@performance
def long_time():
    print("For the first func: long_time()")
    for i in range(100100100):
        i*10


@performance
def long_time2():
    print("For the second func: long_time2()")
    for i in list(range(100100100)):
        i*10


long_time()
long_time2()
