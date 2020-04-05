#!/usr/bin/python3

class BMW:
    def __init__(self, make, year):
        print("BMW INIT")
        self.make = make
        self.year = year
    def start(self):
        print("START")

class E3(BMW, object):
    def __init__(self,x,  make, year):
        print("E3 INIT")
        #BMW.__init__(self, make, year)
        super(E3, self).__init__(make, year) 
        self.x = x
    def start(self):
        super().start()
        print("START2")

x = BMW(1,1)
x.start()

e3 = E3(1,2,3)
print(e3.make)
print(e3.year)
print(e3.x)

e3.start()


