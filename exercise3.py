# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:38:23 2019

@author: Moath
"""

x = [15, 25, 3]

# exercise 1
for item in x:
    print(item)

print('--------------------------')

# exercise 2
print(sum(x))

print('--------------------------')

# exercise 3
print(max(x))

print('--------------------------')

# exercise 4
a = [10,20,30,20,10,50,60,40,80,50,40]
f = set(a)
print(list(f))

print('--------------------------')

# exercise 5
print(len(a))

print('--------------------------')

#exercise 6
new_tuple = (1.7, 15, 'moath', True)
for x in new_tuple:
    print(x)
    
print('--------------------------')

#exercise 7
num_set = set([0, 1, 2, 3, 4, 5])
for s in num_set:
    print(s)
    
print('--------------------------')

# exercise 8
set1 = {"Moath", 1, 1, 2, 2}
set2 = {"Emad", 1, 3, 2, "Moath"}

print(set1 & set2)



print('--------------------------')

#exercise 9
setx =  set(["green", "blue"])
sety =  set(["blue", "yellow"])
seta = setx | sety
print(seta)

print('--------------------------')

#exercise 10
seta = set([5, 10, 3, 15, 2, 20])
print(len(seta))

print('--------------------------')

# exercise 11
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)

print('--------------------------')

# exercise 12
a = 'hello, world!'
print(a[1])
print(a[2:5])
print(a[-5:-2])
print(len(a))
print(a.lower())
print(a.replace("h", "J"))




















