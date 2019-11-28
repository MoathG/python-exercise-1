# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:22:27 2019

@author: Moath
"""
# exercise 1
import pandas as pd
data = [2, 4, 6, 8, 10]
s = pd.Series(data)
print(s)

print('----------------------------------')
# exercise 2
data = [100, 200, 300, 400, 800]
s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print(s)

print('----------------------------------')

# exercise 3
data = [20, 10, 150, 110, 100, 50]
s = pd.Series(data)
#print( s.describe())
s.plot(kind="bar")

print('----------------------------------')

# exercise 4
Data = {'d1':[100,200,5,400,700,100,200,50,400,700],'d2':[140,0,300,400,200,140,0,700,400,200]}

df = pd.DataFrame(Data,columns=["d1", "d2"])

df.plot()

print('----------------------------------')

# exercise 5
d = {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}

df = pd.DataFrame(d)

print(df)

print('----------------------------------')

# exercise 6
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

series = pd.Series(births, index=names, name='series')

print(series) 
series.plot.pie(y='births', figsize=(5, 5))

print('----------------------------------')

d = [100, 2200, 300, 400, 500, 600, 700, 800, 900] 
df = pd.DataFrame(d, columns = ['Number'])
df.to_excel('PandaTest.xlsx', sheet_name = 'testing', index = True)
df.to_csv('myDataFrame.csv', sep='\t')
df.to_csv('myNewData.csv', sep=',')

print('----------------------------------')

# exercise 8
import numpy as np

dates = pd.date_range('20000101', periods = 4)

df = pd.DataFrame(np.random.randn(4, 2), index = dates, columns = ['A', 'B'] )

print(df)
print(df.head(2))
print(df[['A']])
print(df[0:1])
print(df['20000102':'20000104'])
print(df.loc['20000102':'20000104', ['A']])
print(df.iloc[:, 1:2])
print(df[df.B > 0])
df['A'] = [100, 200, 300, 100]
print(df)
print(df[df['A'].isin([200, 300])])













