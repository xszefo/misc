#!/usr/bin/env python
def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

m = yrange(5)


def evennumbers(liczba):
    i = 0
    while(i < liczba):
        #print "i {} liczba {}".format(i,liczba)
        if(i%2==0):
            #print "got it {}".format(i)
            yield i
        i += 1


m = evennumbers(10)


for i in m:
    print i


x = [i*i*i for i in range(5) if i%2==0]
print x

