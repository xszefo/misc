#!/usr/bin/env python


def gen(lista):
    for i in lista:
            if(len(i) > 2):
                yield i


generator = ["test", "test2", "tasdasda", "teasdasdas", "s"]

for i in gen(generator):
    #print i
    pass



for i in generator:
    if(len(i) > 2):
        #print i
        pass


def reverse(linia):
    dlugosc = len(linia)
    for i in range(len(linia)):
        yield linia[dlugosc-i-1]


x = []
for i in reverse("testowy komunikat"):
    x.append(i)
print "".join(x)
