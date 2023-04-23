import functools
import time

def wrapper_time(func):
    def func_wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        t = stop - start
        print(t)
        return result
    return func_wrapper



@wrapper_time
def get_sequence(n):
    
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v
    

print(get_sequence(3))