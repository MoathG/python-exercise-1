# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 13:45:27 2019

@author: Moath
"""

import sqlite3
# =============================================================================
# conn = sqlite3.connect('stocks.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE stocks
#           (data text, trans text, symbol text, qty real, price real)''')
# c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100,35.14)")
# c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'SEL', 'RHAT', 50,35.25)")
# conn.commit()
# conn.close()
# =============================================================================

print('--------------------')

# =============================================================================
# conn = sqlite3.connect('stocks.db')
# 
# c = conn.cursor()
# 
# symbol = 'RHAT'
# c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)
# 
# for row in c:
#     print(row)
# conn.close()
# =============================================================================

print('--------------------')

conn = sqlite3.connect('stocks.db')

c = conn.cursor()
c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'APPLE', 100,4.49)")
c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'SEL', 'APPLE', 50,3.23)")
c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'APPLE', 100,4.49)")
c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'SEL', 'APPLE', 50,3.23)")

conn.commit()
conn.close()

print('--------------------')

# =============================================================================
# conn = sqlite3.connect('stocks.db')
# 
# c = conn.cursor()
# 
# for row in c.execute('SELECT symbol, qty, price FROM stocks ORDER BY price'):
#     print(row)
# conn.close()
# =============================================================================

print('--------------------')

# =============================================================================
# conn = sqlite3.connect('stocks.db')
# c = conn.cursor()
# c.execute('DELETE from stocks where symbol = "APPLE" and price=3.23')
# conn.commit()
# for row in c.execute('SELECT symbol, qty, price FROM stocks ORDER BY price'):
#     print (row)
# conn.close()
# 
# =============================================================================

# =============================================================================
# conn = sqlite3.connect('stocks.db')
# c = conn.cursor()
# c.execute('UPDATE stocks SET qty=10000 where symbol = "RHAT"')
# conn.commit()
# for row in c.execute('SELECT symbol, qty, price FROM stocks ORDER BY price'):
#     print (row)
# conn.close()
# =============================================================================


















