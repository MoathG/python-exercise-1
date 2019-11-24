# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:05:18 2019

@author: Moath
"""
# exercise 1
o = lambda x = 1, y = 2, z = 3: x + y + z
print(o())
print(o(10))
print(o(10, 20)) 

print('-------------------------------------------------')

# exercise 2
from functools import reduce
li = [5, 15, 7, 2, 8, 6]
multi = reduce(lambda a,b: a * b, li)
print(multi)


def multiply(a, b):
    return a * b
multi1 = reduce(multiply, li)
print(multi1)

print('-------------------------------------------------')

#exercise 3
f = (lambda a,b: a * b)
print(f(5, 6))

print('-------------------------------------------------')

# exercsie 4
num_list = range(-5, 5)
print(list(filter(lambda x: x < 0, num_list)))


print('-------------------------------------------------')

# exercise 5
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


print('-------------------------------------------------')

# exercise 6
x = ('Joey', 'Monica', 'Ross')
y = ('Chandler', 'Pheobe')
z = ('David', 'Rachel', 'Courtney')
result = list(zip(x, y, z))
print(result)

print('-------------------------------------------------')

#exercise 7
coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')
d = dict(zip(coin, code))
print(d)

print('-------------------------------------------------')

#exercise 8
# function that filters vowels
def fun(varibale):
    letters = ['a', 'e', 'i', 'o', 'u']
    if(varibale in letters):
        return True
    else:
        return False
    
sequence = ['g', 'j', 'e', 'j', 'k', 'o', 'p', 'r']
filtered = list(filter(fun, sequence))
print(filtered)

print('-------------------------------------------------')

# exercise 9
# =============================================================================
# x = list(map(int, input('Enter a multiple value: ').split()))
# print('List of students: ', x)
# =============================================================================

print('-------------------------------------------------')

#exercise 10
def newfunc(a):
    return a * a
x = list(map(newfunc, (1, 2, 3, 4)))
print(x)

print('-------------------------------------------------')

# exercise 11
def func(a, b):
    return a + b
a = list(map(func, [2, 4, 5], [1, 2, 3, 4]))
print(a)

print('-------------------------------------------------')

# exercise 12
c = map(lambda x: x + x, filter(lambda x: (x >= 3), (1, 2, 3, 4)))
print(list(c))

print('-------------------------------------------------')

# exercise 13
c = filter(lambda x: (x >= 3), map(lambda x : x + x, (1, 2, 3, 4)))
print(list(c))

print('-------------------------------------------------')

# exercise 14
import functools
new_list = [1, 3, 6 , 7, 11]
print('the minimum number of the list is: ', end='')
print(functools.reduce(lambda a,b : a if a < b else b, new_list))

print('-------------------------------------------------')

#exercise 15
numbers = [1, 2, 3]
letters=['a', 'b', 'c']
print(list(zip(numbers, letters)))




















