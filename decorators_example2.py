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
    for i in range(100000):
        i*2


long_time()
