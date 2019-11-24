# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 12:41:03 2019

@author: Moath
"""

# exercise 1
# num1 = int(input('enter the first num: '))
# num2 = int(input('enter the second num: '))
# 
# if num1 > num2 :
#     print(num1)
# else:
#     print(num2)
# =============================================================================

# exercise 2    
# =============================================================================
# num = int(input('enter a num: '))
# 
# for i in range(1, 11):
#     print( num,'*', i, '=' ,num * i)
#     
# =============================================================================


# exercise 3
for i in range(0, 5):
    for j in range(0, i + 1):
        print('*', end=" ")
    print()
    
for i in range(5, 0, -1):
    for j in range(0, i - 1):
        print('*', end=' ')
    print()
    
    
# exercise 4

# =============================================================================
# letters = ['x', 'y', 'z', 'a', 'b', 'c']
# for i in letters:
#     if i == 'a':
#         continue
#     elif i == 'c' :
#         break
#     print(i)
# =============================================================================
    

# exercise 5
# =============================================================================
# for x in range (12, 25, 3) :
#     print(x)
# =============================================================================


#exercise 6
# =============================================================================
# i = 1
# while i < 6 :
#     print(i)
#     if i == 3:
#         break
#     i += 1
# =============================================================================
    

# exercise 7
# =============================================================================
# x = int(input('please enter a number: '))
# for i in range(0, x) :
#     print(i + x)
# =============================================================================
    
# exercise 8
# =============================================================================
# y = int(input('please enter a number: '))
# if y % 2 == 0:
#     print('the number in even')
# else:
#     print('the number is odd')
# =============================================================================


# exercise 10
    
# =============================================================================
# while True:
#     try:
#         x = input("Please enter an integer: ")
#         x = int(x)
#         break
#     except ValueError:
#         print("No valid integer! Please try again ...")
# print("Great, you successfully entered an integer!")
# =============================================================================



 
# exercise 11
# =============================================================================
# try:
#     a = 3
#     if a < 4 :
#         b = a/(a-3)
#     print('Value of b = ',b)
# except(ZeroDivisionError, NameError):
#     print("\nError Occurred and Handled")
# =============================================================================


# =============================================================================
# for i in range(10):
#     for j in range(1, i + 1) :
#         print("*", end=' ')
#     print()
# for i1 in range (10, 0, -1):
#     for j1 in range (i1):
#         print("*", end=' ')
#     print()
# =============================================================================

for i in range(10):
    n = 1
    for j in range(9 - i):
        print(" ", end="  ")
    for j in range(i - 1):
        print(n, end='  ')
        n += 1
    for j in range(i):
        print(i - j, end="  ")
    print()
    
for i in range(9, 0, -1):
    n = 0
    for j in range(10 - i):
        print(' ', end="  ")
        
    for j in range(i - 1):
        print(n + 1, end="  ")
        n += 1
    for j in range((i-1), 1, -1):
       print(j-1, end="  ")
    print()
        












