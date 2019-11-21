# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:38:14 2019

@author: Moath
"""


s1 = 'Hello Orange Academy'

print(s1)
print (s1[0])
print (s1[-2])
print (s1[2:10]) 
print (s1[5:])
print (s1 * 2)
print ( s1.capitalize())
print ( s1.upper())
print (s1.center(100))
print (s1.replace('Orange', 'Amman'))
print ('      world         '.strip()  )
s2='#'.join(['hello','Orange'])
print(s2)

list1 = [1, 20, -1, 0,1000]
list2 = [23, 546]
list1.extend(list2)
print(list1)
print(len(list1))
print(min(list1))
print(max(list1))
print(sorted(list1))
print(sum(list1))

list1.sort()
list1.pop()
print(list1)

list2 = list1[:]
print(list2)

list3 = list1.copy()
print('list3: ', list3)


m = (14, 1, 'moath', 'hello', True)
print(m)

my_list = ['a', 'b']
t1 = ('apple',)
t2 = t1 + (1,2,3) + tuple(my_list)
print(t2)
print(t2[0])
print(t2[1:4])

print('--------------------------')

t1=(1,['a','b','c']) 
t1[1][0] = 'd' 
print (t1) 
del t1 
t1=1,2,3,4 
print (t1)

print('--------------------------')

s1={"Apple","Apple",1,1,1,2,(1,2),(1,2)}
print(s1)

print('--------------------------')

print(list(set([1,1,2,3,4,2,2,2,2,])))

print('--------------------------')

s1=set("abcdef")
s2=set("efghi")
print ( s1 | s2 )
print ( s1 & s2 )
print ( s1 - s2 )
print ( s1 ^ s2 )

print('--------------------------')

student = {
    'name': 'moath',
    'age' : 25,
    'degree' : 92        
}
print(student)
for x in student:
    print(x)
    
for x in student:
    print(student[x])
    
for x, y in student.items():
    print(x,y)

if 'degree' in student:
    print('yes, degree in the student dictionary')
    
student['nationality'] = 'jordanian'
print(student)

student.pop('nationality')
print(student)

print('--------------------------')





















