#!/usr/bin/python3

class MyClass:
   
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Name: {}'.format(self.name)

    @property
    def hello_name(self):
        return 'Hello {}'.format(self.name)

    @hello_name.setter
    def hello_name(self, string):
        hello, name = string.split()
        self.name = name

    @hello_name.deleter
    def hello_name(self):
        print('Delete: {}'.format(self.hello_name))

a = MyClass('Piotr')

print(a)
print(a.hello_name)

a.hello_name = 'Hello Monika'

print(a)
print(a.hello_name)


del a.hello_name
