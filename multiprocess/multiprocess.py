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
    futs = [ executor.submit(funkcja, arg) for arg in range(1,11)]
    for fut in concurrent.futures.as_completed(futs):
        print('Wynik as_completed: {}'.format(fut.result()))

t2 = time.time()

print(f'Czas: {t2-t1}')

with concurrent.futures.ProcessPoolExecutor() as executor:
    wyniki = executor.map(funkcja, range(1,11)) 
    for wynik in wyniki:
        print('Wynik map: {}'.format(wynik))


t3 = time.time()

print(f'Czas: {t3-t2}')


print(f'Calkowity czas wykonania: {t3-t1}') 
