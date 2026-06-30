
# pandas

import pandas as pd
import numpy as np

# create 1D array using Series()
a = pd.Series([1,2,3])
a
 
# create 1D array using Series() & changing index
a = pd.Series([1,2,3],index = ("a","b","c"))
a

# create 2D array using DataFrame()

a = pd.DataFrame([1,2,3,4,5,6],columns= ['value'],index = ['a','b','c','d','e','f'])
a


data = pd.DataFrame({'India':[10,20,30,40],'USA': [40,50,60,70],'UK': [100,200,300,400]})
print(data)


# Concept of indexing
# using descriptive stats to calculate the data
data['India'].sum(),data['India'].mean(),data['India'].median(),data['India'].max(),data['India'].min()
 

# calculate IQR and also Q1 and Q3 for column India 

Q1 = data['India'].quantile(0.25)
Q3 = data['India'].quantile(0.75)

IQR = Q3 - Q1

UW = Q3 + 1.5*IQR
LW = Q1 - 1.5*IQR

print(Q1,Q3,IQR,UW,LW)
 

# calculate skewness and kurtosis

skewness_India = data['India'].skew()
skewness_India
 

kurtosis_India = data['India'].kurt()
kurtosis_India  
 

import matplotlib.pyplot as plt
data['India'].plot(kind = 'kde')
plt.axvline(25,color = 'r', linestyle = '--')
plt.axvline(32.5,color = 'g', linestyle = '--')
plt.axvline(17.5,color = 'g', linestyle = '--')
plt.axhline(0.005,color = 'b',linestyle = '--')
plt.show()
 

# .head() provides required rows from top
data.head(3)

 

# .tail provides required rows from bottom
data.tail(3)
 

# data gets shuffeled ::: 1 means 100% suffle
data.sample(frac = 1)
 

# checking dataset information and description stats
'''
data.info(): guides us following parameters
1.no of rows 
2.no.of colums
3.datatype of each column
'''
data.info()
 

# derives desciptive stats
data.describe()
 

# chaecking Null values in dataset using stats method 

data.isnull().sum()
 

# checking Null values in dataset using graphical method

data.isnull().sum().plot(kind = 'bar')
plt.title('The plot shows Null values present in columns')
plt.show()

 

print(data)

# data.iloc[row_index,column_index]
data.iloc[2,2]
 

# data filter
data[data['UK'] > 300]
 

df = pd.DataFrame({'Gender':['Male','Female','Male','Female'],
                   'Station':['Thane', 'Bhandup','Kalyan','Diva'],
                   'Age': [50,70,90,45],
                   'Salary':[1000,3000,5000,7000]})
df

male_data = df[df['Gender'] == 'Male']
male_data

female_data = df[df['Gender'] == 'Female']
female_data

df['Gender'].value_counts().plot(kind = 'pie', autopct = '%0.2f',explode = [0.015,0.015])

plt.title('gender Distribution')
plt.show()
