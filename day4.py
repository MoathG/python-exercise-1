# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 09:30:43 2019

@author: Moath
"""

def moath_name(name = "gharib") :
    print('my name is ' + name)

moath_name('moath')
moath_name('emad')
moath_name()


# ============================================================

def my_function(food) :
    for x in food:
        print(x)
        
fruits = ['apple', 'banana', 'cherry']

my_function(fruits)

# ============================================================

def my_function1(x):
    return 5 * x

print(my_function1(3))
print(my_function1(5))
print(my_function1(9))



# =============================================================

def my_function2(child3, child2, child1):
    print('the youngest child is ' + child3)
    
my_function2(child1 = 'sam', child2 = 'Tobais', child3 = 'Khalid')


# =============================================================

def adder (*num) :
    sum = 0
    for n in num:
        sum = sum + n
    print("Sum: ", sum)
    
adder(3, 5)
adder(4, 5, 6, 7)
adder(1, 2, 3, 5, 6)

# ============================================================

def myFun(arg1, *arg):
    print('first argumant ' + arg1)
    
    for n in arg:
        print('Next argumant through *arg :', n)
        
myFun('hello', 'welcome', 'to', 'GeeksforGeeks')

 # ==========================================================
 

def area (*args) :
    return args[0]*args[1]/2

print(area(10, 30))


# ============================================================

def some_args(arg1, arg2, arg3):
    print('argumaent1 :' , arg1)
    print('argumaent2 :' , arg2)
    print('argumaent3 :' , arg3)

my_list = [2, 3]
some_args(1, *my_list)

# ============================================================


def sqoor (**kwargs) :
    for key, value in kwargs.items() :
        print('%s == %s' %(key, value))
        
sqoor(first = 'moath', mid = 'emad', last = 'gharib')


# ===========================================================

x = 'awesome'

def myfun() :
    global x
    x = 'fantastic'
    print('Python is ' + x)
    
myfun()
print('Python is: ' + x)


# ========================================================

def factorial(n) :
    if n == 1 :
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(10))

# ======================================================

sum = lambda x, y, z : x + y + z
print(sum(56, 7, 2))

m = (lambda  m, y : m + y)(2, 3)
print(m)

print((lambda x, y: x + y) (2,3))

print((lambda x, y, z = 3: x + y + z)(1, 2))

# ====================================================

my_pets = ['cat', 'dog', 'turtul', 'bird']
uppered_pets = list (map(str.upper, my_pets))
print(uppered_pets)

# ===================================================

print(list(map(lambda x : x.upper(), ['cat', 'dog', 'cow'])))

# ==================================================

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2, li))
print(final_list)

# =================================================

MyList = [0,1,2,3,4,10,13,22,25,100,120]
print('squared list: ', list(map(lambda x: x**2, MyList)))

# =================================================

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1, 7)))
print(result)

# ================================================

sentence = 'AlZytonah University of Jordan '
print(list(map(lambda word: len(word), sentence.split())))

# ================================================

filtered = list( filter(lambda x: x % 2 == 0, range(0,11)))
print(filtered)

# ================================================

MyList = [0,1,2,3,4,10,13,22,25,100,120]
odd_numbers = list(filter(lambda x: x % 2, MyList))
print(odd_numbers)

# ================================================

even_numbers = list(filter(lambda x: x % 2 == 0, MyList))
print(even_numbers)

# ================================================

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score > 75
over_75 = list(filter(is_A_student, scores))
print(over_75)

print(list(filter(lambda score: score > 75, scores)))



my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]
my_digits = ['y', 'i', 'r', 't', 'q']
results = list(zip(my_strings, my_numbers, my_digits))
print(results)


from functools import reduce
x = reduce(lambda a,b : a + b, [23, 21, 45, 98])
print(x)

lis = [1, 3, 5, 6, 2]

import functools
# using reduce to compute sum of list
print('the sum of the list elements is: ', end = '')
print(functools.reduce(lambda a,b : a + b, lis))

# using reduce to compute maximum element from list
print ("The maximum element of the list is : ",end="")
print (functools.reduce(lambda a,b : a if a > b else b,lis)) 






















































