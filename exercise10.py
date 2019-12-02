# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:18:28 2019

@author: Moath
"""
# example 1
from sympy import *
from sympy.plotting import *

x,y,z = symbols('x y z')

# A
expr= x**2+x**3+21*x**4 + 10*x+1
print( expr.subs(x, 7) )

print('----------------------------------')

# B
print(expand( (x + y) ** 2))

print('----------------------------------')

# C
print(simplify(4*x**3+21*x**2+10*x+12))

print('----------------------------------')

# D
print(limit(1/(x**2),x,oo))

print('----------------------------------')

# F
print(integrate(sin(x)+exp(x)*cos(x)+tan(x),x))

print('----------------------------------')

# G
print(factor(x**3 + 12*x*y*z +3*y**2*z) )

print('----------------------------------')

# H
print(solveset(x-4,x))

print('----------------------------------')

# I
m1 =Matrix([[5, 12, 40], [30, 70, 2]])
m2 =Matrix([2, 1, 0])
print( m1*m2 )

print('----------------------------------')

# J
plot(x**3+3, (x, -10, 10))

print('----------------------------------')

# K
f=x**2*y**3
plot3d(f, (x, -6, 6), (y, -6, 6))


import xlsxwriter

workbook = xlsxwriter.Workbook('example1.xlsx')
worksheet = workbook.add_worksheet()

worksheet.autofilter('A1:B4')

data = ['This is Example', 'My first export example', 1, 2, 3]

format = workbook.add_format()
format.set_bold()
format.set_font_color('red')
format.set_font_size(20)

worksheet.write_column('A1', data, format)
worksheet.write_comment('B1', 'This is a comment')

format2 = workbook.add_format({'bold' : True, 'font_color': 'blue'})
worksheet.write_column('B1', data, format2)

workbook.close()

print('----------------------------------')

# example 2
import xlsxwriter

workbook = xlsxwriter.Workbook('example10.xlsx')
worksheet = workbook.add_worksheet()
worksheet.autofilter('A1:B1')

data = ["this is example"]

format = workbook.add_format()
format.set_font_color('red')
format.set_font_size(12)

worksheet.write_column('A1:B1', data ,format)

data2 = ["export my sheet"]

format = workbook.add_format()
format.set_font_color('black')
format.set_font_size(12)

worksheet.write_column('A2:B2', data2 ,format)

data3=[1,2]

data4=[3]

for elem in data3:
    format = workbook.add_format()
    format.set_font_color('black')
    format.set_font_size(12)
    worksheet.write_column("A3:A4", data3 ,format)

for elem in data4:
    format = workbook.add_format()
    format.set_font_color('red')
    format.set_font_size(12)
    worksheet.write_column("A5", data4 ,format)

workbook.close()

print('----------------------------------')


from xlrd import open_workbook
wb = open_workbook('simple.xlsx')
for s in wb.sheets():
    print ("Sheet:", s.name)
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print(values)









