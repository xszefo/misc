#!/usr/bin/python3

class Deskryptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, objtype):
        return obj.__dict__[self.name]
    
    def __set__(self, obj, val):
        obj.__dict__[self.name] = val

class MyClass:
    x = Deskryptor('x')
   
    def __init__(self):
        self.x = 5
    def __str__(self):
        return str(self.x)

a = MyClass()
b = MyClass()

print(a.x)
print(b.x)
a.x = 7
print(a.x)
print(b.x)

b.x = 10

print(a)
print(b)



