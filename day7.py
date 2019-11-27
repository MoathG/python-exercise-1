# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 09:59:21 2019

@author: Moath
"""

import numpy as np
b = np.array([1, 4, 7, 5])
print(b)

print('---------------------------------------------')

c = np.array([[1, 4, 7, 5], [2, 8, 3, 2]])
print(c)

print('---------------------------------------------')

a = np.arange(12).reshape(3, 4)
print(a)
print('a size: ', a.size)
print('a shape: ', a.shape)
print('a ndim: ', a.ndim)
print('a dtype.name: ', a.dtype.name)
print('a itemsize: ', a.itemsize)


print('---------------------------------------------')

d = np.array([(1.5, 2, 3), (4, 5, 6)])
print(d)
print('d shape: ', d.shape)

print('---------------------------------------------')

f = np.array([[1, 2], [3, 4]], dtype=complex)
print(f)

print('---------------------------------------------')

e = np.zeros((4, 10))
print(e)

print('---------------------------------------------')

g = np.ones((2, 4), dtype = np.int16)
print(g)

print('---------------------------------------------')

j = np.arange(24).reshape(2, 3, 4)
print(j)
print('j shape: ', j.shape)
print('j ndim: ', j.ndim)

print('---------------------------------------------')

a = np.array([[3,7,2,1,8,7,19,15],[10,2,7,4,5,5, 9,1]])
print('a array:') 
print (a) 
print('\n quicksort:') 
print (np.sort(a,kind='quicksort') ) 
print('\n mergesort') 
print (np.sort(a,kind='mergesort') ) 
print('\n heapsort:') 
print (np.sort(a,kind='heapsort') ) 
print('\n sort as flattened arra:') 
print (np.sort(a,axis=None) )

print('---------------------------------------------')

import numpy as np
import matplotlib.pyplot as plt
def mandelbrot(h, w, maxit = 20):
    y,x = np.ogrid[-1.4:1.4:h*1j, -2:0.8:w*1j]
    c = x + y * 1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype = int)
    
    for i in range(maxit):
        z = z ** 2 + c
        diverge = z*np.conj(z) > 2 ** 2
        div_now = diverge & (divtime == maxit)
        divtime[div_now] = i
        z[diverge] = 2
        
    return divtime
plt.imshow(mandelbrot(400, 400))
plt.show()

print('---------------------------------------------')


import matplotlib.pyplot as plt
f = [1, 2, 8, 4, 5, 6]
plt.plot(f)
plt.show()

print('---------------------------------------------')

plt.style.use('ggplot')

x = [1, 2, 3, 4, 5, 6]
y = [1, 4, 9, 16, 0, 30]

plt.plot(x, y)
plt.ylabel('Y Numbers')
plt.xlabel('X Numbers')
plt.show()

print('---------------------------------------------')

import numpy as np 
import matplotlib.pyplot as plt
def p1(x): return x**4 - 4*x**2 + 3*x 
def p2(x): return np.sin(10*x) * 10 
X = np.linspace(-3, 3, 200)
plt.plot( X,p1(X), X,p2(X)) 
plt.show()

print('---------------------------------------------')

import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.005) 
y = np.exp(-x/2.) * np.sin(2*np.pi*x)

plt.plot(x, y) 
plt.xlim(0, 10) 
plt.ylim(-1, 1) 
plt.show()

print('---------------------------------------------')

import numpy as np 
import matplotlib.pyplot as plt

x=np.arange(0.,10,0.1) 
a=np.cos(x) 
b=np.sin(x) 
c=np.exp(x/10) 
d=np.exp(-x/10)

plt.plot(x,a,'b-',label='cosine') 
plt.plot(x,b,'r--',label='sine') 
plt.plot(x,c,'g-',label='exp(+x)') 
plt.plot(x,d,'y',linewidth=5,label='exp(-x)')

plt.legend(loc='upperleft') 
plt.xlabel('xaxis') 
plt.ylabel('yaxis') 
plt.show()

print('---------------------------------------------')

import numpy as np 
import matplotlib.pyplot as plt
n = 1024 
X = np.random.normal(0,1,n) 
Y = np.random.normal(0,1,n)
plt.scatter(X,Y) 
plt.show()

print('---------------------------------------------')

import matplotlib.pyplot as plt 
import numpy as np 
x = np.arange(-2*np.pi,2*np.pi,0.01) 
y = np.sin(3*x)/x 
y2 = np.sin(2*x)/x 
y3 = np.sin(x)/x 
plt.plot(x,y) 
plt.plot(x,y2) 
plt.plot(x,y3)

print('---------------------------------------------')

import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-2, 2, 400) 
y = x.copy() 
X, Y = np.meshgrid(x, y) 
Z = np.exp(-(X**2 + Y**2))
fig, ax = plt.subplots(nrows=2, ncols=2, subplot_kw={'projection': '3d'})

ax[0,0].plot_wireframe(X, Y, Z, rstride=40, cstride=40) 
ax[0,1].plot_surface(X, Y, Z, rstride=40, cstride=40, color='m') 
ax[1,0].plot_surface(X, Y, Z, rstride=12, cstride=12, color='m') 
ax[1,1].plot_surface(X, Y, Z, rstride=20, cstride=20, cmap='hot')

fig.tight_layout() 
plt.show()














