# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Wed Nov 20 09:33:27 2019
# 
# @author: Moath
# """
# 
# a,b = 1,10
# if a > b:
#     print('a > b')
# elif a < b:
#     print('a < b')
# else:
#     print('a = b')
# 
#     
# max = a if (a > b) else b
# print(max)
# 
# 
# if 'a' in ['b', 'c', 'a']:
#     print("a in the list")
# else: print("a not in the list")
# 
# 
# if a > b: print("a is greater than b")
# 
# print("A" if a > b else print("B"))
# 
# a = 1000
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")
# 
# 
# x = int(input('please inter first num: '))
# b = int(input('please inter second num: '))
# 
# if (x > b):
#     print(b, x)
# else:
#     print(x,b)
#     
# 
# name = input('please inter your name: ')
# age = int(input('please inter your age: '))
# 
# if age < 18:
#     print('under age')
#     school_avg = float(input('please inter your avg: '))
#     if school_avg >= 90:
#         print('Excellent Avergae')
#     elif school_avg >= 50 and school_avg < 90:
#         print('Passed')
#     else:
#         print('Failed')
# else:
#     job = input('please inter your job title')
#     print (str(age), name, job)
#     

# =============================================================================
# for a in range (3):
#     print(a)
# =============================================================================

#the first number is where the itiration begin
#the second number is where the itiration end
#the third number is the steps or the added number
for a in range (1, 6, 2):
    print(a)


for x in 'moath':
    print(x)
    
for s in ['moath', 'emad', 'gharib']:
    print(s)
    

fruits = ['apple', 'banana', 'cherry']
for m in fruits:
    if m == 'banana':
        continue
    print(m)


for n in range (6):
    print(n)
else:
    print('Finnally finished')
    


color = ['red', 'blue', 'black']

for c in color :
    for v in fruits :
        print (c, v)
        

words = ['cat', 'window', 'defenestrate' ]

for u in words :
    print(u, len(u))
    
    
l = ['eat', 'sleep', 'repeat', 'welcome']

for count,e in enumerate(l) :
    print(count,e)

# =============================================================================
# while True:
#     a = input('>')
#     if a == 'exit' :
#         break
#     print(a)
# =============================================================================

colors = ['red', 'green', 'blue', 'purple']
i = 0
while i < len(colors) :
    print(colors[i])
    i += 1

# 1
# =============================================================================
# for q in range(10):
#     print('*')
# =============================================================================

# 2
# =============================================================================
# for u in range (10):
#     print('*', end=' ')
# =============================================================================
    
for asd in range(1):
    for dsa in range(10):
        print('*' * dsa)

for i in range(10):
    for j in range(i):
        print('*', end='')
    print()
    
# =============================================================================
# k = 10
# for i in range (0, 10):
#     for j in range (0, k):
#         print(end=" ")
#     k = k - 2
#     for j in range (0, i+1):
#         print('* ', end="")
#     print()
# =============================================================================
    
    
while True:
    try:
        n = input('please enter an integer: ')
        n = int(n)
        break
    except ValueError:
        print('No valid integer! Please try again ...')
print('Great, you successfuly entered an integer!')

try:
    x = float(input('Your number: '))
    inverse = 1.0 / x
except ValueError:
    print('You should have given either an int or float')
except ZeroDivisionError:
    print('Infinity')
finally:
    print('There may or may not have been an excption.')
    
    
















