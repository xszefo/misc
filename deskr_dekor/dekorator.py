#!/usr/bin/python3

def wrapper(func):
    def nowa(*args, **kwargs):
        print(kwargs)
        func(*args, **kwargs)
        
    nowa.__name__ = func.__name__
    return nowa

@wrapper
def funkcja(x='1',y='2'):
    print(x)
    print(y)

#funkcja(x = '1', y = '2')




def count(func):
    counter = 0
    def nowa(*args, **kwargs):
        nonlocal counter
        counter += 1
        nowa.liczba += 1
        func(*args, **kwargs)
    nowa.liczba = 0
    nowa.__name__ = func.__name__
    return nowa

@count
def funkcja_testowa():
    print("TEST")

for i in range(0,15):
    print(funkcja_testowa.__dict__)

    funkcja_testowa()

print(funkcja_testowa.__dict__)
print(funkcja_testowa.__name__)
