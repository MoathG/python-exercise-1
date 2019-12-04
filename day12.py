# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:35:43 2019

@author: Moath
"""

test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key = test.count))

print('--------------------------')

a = [1, 2, 3, 4, 5]
a[2:3] = [0, 0]
print('\n', a)

print('--------------------------')

import itertools

for p in itertools.permutations([1, 2, 3, 4]):
    print(p, " > ", ''.join(str(x) for x in p))
    
print('--------------------------')

x = list(itertools.permutations('ab'))
print(x)