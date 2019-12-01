# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 09:29:10 2019

@author: Moath
"""

import statistics as st

x = [3, 1.5, 4.5, 6.75, 2.25, 5.75, 2.25]

print(st.mean(x))
print(st.harmonic_mean(x))
print(st.median(x))
print(st.median_low(x))
print(st.median_high(x))
print(st.median_grouped(x))
print(st.mode(x))
print(st.pstdev(x))
print(st.pvariance(x))
print(st.stdev(x))
print(st.variance(x))

print('----------------------------')

import random

print(random.random())
print(random.randrange(100))
print(random.choice(['Jordan', 'USA', 'UK']))
print(random.sample(range(100), 5))
print(random.choice('abcdefghij'))

items = [11, 12, 30, 14, 35, 66, 17]
random.shuffle(items)
print(items)

print(random.randint(10, 20))
print ( random.randrange(0, 101, 2) )
print  ( random.uniform(1, 100))

print('----------------------------')

import math
print ('pi: %.40f' % math.pi) 
print ('e: %.40f' % math.e)

print('----------------------------')

import doctest
def sum (a,b):
    """
    Calculates the sum of a and b
    >>> sum (1,1)
    2
    >>> sum(1,-1)
    0
    >>> sum (-1,-1)
    -2
    >>> sum(0,-10)
    -10
    >>>
    """
    return a+b

if __name__=="__main__":
    doctest.testmod()

print('----------------------------')

from PIL import Image

# =============================================================================
# im = Image.open('photo.jpg')
# print(im.format, im.size, im.mode)
# im.show()
# =============================================================================

from PIL import Image, ImageFilter

# =============================================================================
# original = Image.open('photo.jpg')
# blurred = original.filter(ImageFilter.BLUR)
# 
# original.show()
# blurred.show()
# 
# blurred.save('blurred.png')
# =============================================================================

# =============================================================================
# size = (128, 128)
# saved = 'photo.jpg'
# 
# try:
#     im = Image.open('photo.jpg')
# except:
#     print('Unable to load image')
#     
# im.thumbnail(size)
# im.save(saved)
# im.show()
# 
# =============================================================================

# =============================================================================
# image = Image.open('photo.jpg')
# grayscale_image = image.convert('L')
# greyscale_image.show()
# =============================================================================

# =============================================================================
# original = Image.open('photo.jpg')
# newImage = original.filter(ImageFilter.CONTOUR)
# newImage.show()
# =============================================================================

# =============================================================================
# original = Image.open('photo.jpg')
# newimage = original.filter(ImageFilter.SMOOTH)
# newimage.show()
# =============================================================================

# =============================================================================
# original = Image.open('photo.jpg')
# cropped = original.crop((0, 0, 200, 200))
# cropped.show()
# =============================================================================

from PIL import Image
from PIL import ImageDraw

# =============================================================================
# im = Image.open('photo.jpg')
# draw = ImageDraw.Draw(im)
# draw.line((0, 0) + im.size, fill = (255, 255, 255))
# draw.line((0, im.size[1], im.size[0], 0), fill = (255, 255, 255))
# draw.text((im.size[0] / 2 - im.size[0] / 2, im.size[1] / 2 - 60), 'Hussam', fill = (255, 255, 0))
# draw.text((im.size[0] / 2 - im.size[0] / 2, im.size[1] / 2 - 60), 'I mage', fill = (255, 255, 0))
# im.show()
# =============================================================================

# =============================================================================
# original = Image.open('photo.jpg')
# original = original.resize((500, 500))
# original.show()
# =============================================================================


# =============================================================================
# image = Image.open('photo.jpg')
# logo = Image.open('logo.jpg')
# image_copy = image.copy()
# position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
# image_copy.paste(logo, position)
# image_copy.show()
# =============================================================================

# =============================================================================
# image = Image.open('photo.jpg')
# image_rot_90 = image.rotate(90)
# image_rot_90.show()
# =============================================================================

img = Image.open('photo.jpg')
r, g, b = img.split()
Image.merge('RGB', (b, g, r)).save('Image_merge_01.jpg')
im = Image.open('Image_merge_01.jpg')
im.show()



































