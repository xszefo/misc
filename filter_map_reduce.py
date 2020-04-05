#!/usr/bin/python3
from functools import reduce

x = [1,5,3]
print(x)
y = map(lambda a: 2*a, x)
print(y)
print(list(y))

z = filter(lambda a: a%2!=0, x)
print(z)
print(list(z))

def red(a,b):
    print(a)
    print(b)
    print(10*"*")
    return a+b

print(reduce(red, x))
