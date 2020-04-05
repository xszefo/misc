#!/usr/bin/python3
class C:
     @staticmethod
     def metoda():
          print("hi")
obj = C()
obj.metoda()
C.metoda() # moge tez wywolac na klasie, a nie na obiekcie


sentence = 'This is a test'
for word in sentence.split():
    print(word)



