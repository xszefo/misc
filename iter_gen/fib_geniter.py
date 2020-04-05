#!/usr/bin/python3
from time import time

def fibgen(num):
    a = 1
    b = 1
    index = 1
    while True:
        if index > num:
            break
        yield a
        a, b = b, a+b
        index += 1

start = time()
for a,b in enumerate(fibgen(100000)):
    pass
    #print(a+1,b)

print('Time: {}'.format(time() - start))

class FibGen:
    def __init__(self, num):
        self.num = num
        self.a = 0
        self.b = 1
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        self.index += 1
        if self.index > self.num:
            raise StopIteration
        #self.a, self.b = self.b, self.a + self.b
        return self.a

start = time()
for a,b in enumerate(FibGen(100000)):
    pass
    #print(a+1,b)

print('Time: {}'.format(time() - start))

