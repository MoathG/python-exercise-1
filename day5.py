# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 09:37:19 2019

@author: Moath
"""


class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('hello')

    def say_hi(self, m):
        print('hi', m)

    def whoami(self):
        return 'I am ' + self.name

    def __del__(self):
        print('I have been deleted')

# =============================================================================
# p = Person('tom')
# p.say_hello()
# p.say_hi('moath')
# =============================================================================


p1 = Person('tom')
print(p1.whoami())
print(p1.name)
del p1


class Encapsulation(object):
    def __init__(self, a, b, c):
        self.Apublic = a
        self._Bprotected = b
        self.__Cprivate = c

    def getPrivate(self):
        return self.__Cprivate

    def setPrivate(self, value):
        self.__Cprivate = value


x = Encapsulation(11, 13, 17)
print(x.Apublic)
print(x._Bprotected)
x.setPrivate('updated value')
print(x.getPrivate())



class Circle:

    def __init__(self, radius):
        self.__radius = radius

    def setRadius(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius
    
    def __add__(self, another_circle):
        return Circle(self.__radius + another_circle.__radius)
    
c1 = Circle(4)
print(c1.getRadius())

c2 = Circle(5)
print(c2.getRadius())

c3 = c2 + c1
print(c3.getRadius())






































