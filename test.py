# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:05:33 2019

@author: Moath
"""

import sqlite3
conn = sqlite3.connect('stocks.db')

c = conn.cursor()

symbol = 'RHAT'
c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

for row in c:
    print(row)
conn.close()