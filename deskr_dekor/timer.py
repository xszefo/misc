#!/usr/bin/python3

from time import time,sleep

def timer(func):
    def wrapper(*args, **kwargs):
        print('{} + {}, delay: {}'.format(args[0], args[1], args[2]))
        start = time()
        result = func(*args)
        stop = time()
        wrapper.time_elapsed = stop-start
        #print('Time elapsed: {}.'.format(stop-start))
        return result
    # Ponizsza zmienna zawiera ostatni wynik i znajduje sie w slowniku funkcji
    wrapper.time_elapsed = 0
    return wrapper


@timer
def add(x,y,delay):
    sleep(delay)
    return x+y

print(add(3,4,2))
print(add.__dict__)

print()

print(add(6,9,1))
print(add.__dict__)
