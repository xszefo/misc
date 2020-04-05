#!/usr/bin/python3

from time import time,sleep

def decorator(n):
    def middle(func):
        def wrapper(*args, **kwargs):
            print('Argument dekoratora: {}'.format(n))
            print('Argumenty funkcji: {}'.format(args))
            return func(*args, **kwargs)
        return wrapper
    return middle

@decorator(5)
def add(a,b):
    return a+b

@decorator(2)
def mul(a,b):
    return a*b


#add = dekorator(n)(add)

print('Wynik a+b: {}'.format(add(2,3)))
print()
print('Wynik a*b: {}'.format(mul(3,3)))
