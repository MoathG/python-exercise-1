# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 09:38:11 2019

@author: Moath
"""

import pandas as pd
data = [100, 120, 140, 180, 200, 210, 214]
s = pd.Series(data)
print(s)

print('----------------------------------')

data = [100, 120, 140, 180, 200, 210, 214]
s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(s)

print('----------------------------------')

data = [100, 120, 140, 180, 200, 210, 214]

s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

print(s)
print(s.index)
print(s.values)
print(s[0])
print(s['b'])
print(s['f'], s['g'])
print(sum(s))
print(s.head())
print(s.head(3))
print(s.tail())

print('----------------------------------')

data = [100, 120, 140, 180, 200, 210, 214]

s = pd.Series(data)

print(s.describe())
print("mean :", s.mean())
print("std :", s.std())
print(s.agg(['sum', 'max']))
s.plot(kind="bar")
# you can use pie kind
# s.plot(kind="pie")
# s.plot()

print('----------------------------------')

s1 = pd.Series([10, 20, 30, 40, 50, 60],
               index=pd.date_range('20130102', periods=6))
print(s1)
print(s1[0])
print(s1[1:3])
print(s1 > 20)
s1[2] = 999
print(s1[2])

print('----------------------------------')


s = pd.Series([100, 120, 140, 180, 200, 210, 214])
print(s)

s2 = s.apply(lambda x: x if x > 180 else x*10)
print(s2)

s3 = s2[s2 > 1000]
print(s3)

print('----------------------------------')

data = {'apples': [3, 2, 0, 1], 'oranges': [0, 3, 7, 2]}
purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])

print(purchases)
print(purchases.describe())

print('----------------------------------')

XYZ_web= {'Day':[1,2,3,4,5,6], "Visitors":[1000, 700,6000,1000,400,350], "Bounce_Rate":[20,20, 23,15,10,34]}

df= pd.DataFrame(XYZ_web)

print(df)
print(df.head(2))
print(df.tail(2))

# to change a column name
df = df.rename(columns={"Visitors": "Users"})
print(df)

print('----------------------------------')

df1 = pd.DataFrame({ "HPI":[80,90,70,60], "Int_Rate":[2,1,2,3], "IND_GDP":[50,45,45,67]}, index=[2001, 2002,2003,2004])

df2 = pd.DataFrame({ "HPI":[80,90,70,60], "Int_Rate":[2,1,2,3], "IND_GDP":[50,45,45,67]}, index=[2005, 2006,2007,2008])

concat= pd.concat([df1,df2])
print(concat)

print('----------------------------------')

import numpy as np 
import pandas as pd

dates = pd.date_range('20190101', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=list('PQRS'))

print(df.head())
print(df['P'])

print('----------------------------------')

dates = pd.date_range('20190101', periods=8) 
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=list('PQRS')) 

print(df.head()) 
print(df[0:1]) 
print(df['20190102':'20190104'])
print(df[['P','Q']])
print(df.loc['20190102':'20190104', ['P', 'Q']])
print(df.iloc[:, 1:3])
print(df.iloc[0, 1]) 
print(df.iloc[1:3, :])
print(df[df > 0])
print('---')
print(df[df.P > 0])
df['P'] = [100,200,300,100,250,200,600,700]
print(df)

print(df[df['P'].isin([200, 700])])

df.at[dates[0], 'P'] = 0.0
df.iat[0, 2] = 999.0
df.loc[:, 'S'] = np.array([5] * len(df))
print(df)

print('----------------------------------')

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"], "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"], "area": [8.516, 17.10, 3.286, 9.597, 1.221], "population": [200.4, 143.5, 1252, 1357, 52.98] }

my_data = pd.DataFrame(dict)

print("mean :",my_data.mean())
print(my_data.describe())
my_data.index = ["BR", "RU", "IN", "CH", "SA"] 
print(my_data)

print('----------------------------------')

d = {'one':[1,2,3,4,5], 'two':[2,2,2,2,2], 'letter':['a','a','b','b','c']}

df = pd.DataFrame(d)

for index, row in df.iterrows() : 
    print(row['two']+3, row['letter'])

print('----------------------------------')

d = [1,2,3,4,5,6,7,8,9] 
df = pd.DataFrame(d, columns = ['Number'])

df.to_excel('PandaTest.xlsx', sheet_name = 'testing', index = True)

df.to_csv('myDataFrame.csv', sep='\t')

print('----------------------------------')

















