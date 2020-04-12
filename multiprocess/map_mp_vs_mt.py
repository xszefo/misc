#!/usr/bin/python3

import time
import random
import concurrent.futures

def funkcja(x):
    #time.sleep(random.randint(1,3))
    time.sleep(1)
    return x

t1 = time.time()

with concurrent.futures.ProcessPoolExecutor() as executor:
    futs = executor.map(funkcja, range(1,11))
    #for fut in concurrent.futures.as_completed(futs):
    #    print('Wynik as_completed: {}'.format(fut.result()))

t2 = time.time()

mp_time = t2-t1


with concurrent.futures.ThreadPoolExecutor() as executor:
    futs = executor.map(funkcja, range(1,11))
    #for fut in concurrent.futures.as_completed(futs):
    #    print('Wynik as_completed: {}'.format(fut.result()))

t3 = time.time()

mt_time = t3-t2

print('''
Multithreading: {}
Multiprocessing: {}
'''.format(mt_time, mp_time))
