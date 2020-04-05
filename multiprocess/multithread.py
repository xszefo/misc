#!/usr/bin/python3

import time
import random
import concurrent.futures

def funkcja(x):
    time.sleep(random.randint(1,3))
    return x


with concurrent.futures.ThreadPoolExecutor() as executor:
    futs = [ executor.submit(funkcja, arg) for arg in range(1,11)]
    for fut in concurrent.futures.as_completed(futs):
        print('Wynik as_completed: {}'.format(fut.result()))



with concurrent.futures.ThreadPoolExecutor() as executor:
    wyniki = executor.map(funkcja, range(1,11)) 
    for wynik in wyniki:
        print('Wynik map: {}'.format(wynik))


