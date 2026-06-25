import numpy as np
array = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]).reshape(4,5)
array

array[1:3,-2:]

array[1:3,3:]

# stats

'''
1.Decriptive stats: count,max,min,avg,kurtosis,skewness,std,variance etc...
2.Inferential stats: Hyothesis Testing
'''

'''
statics mainly consists of following steps...
step1: collect data
step2: organize data
step3: sumarize data
step4: inferential stats (interpret data)
'''

'''
Central tendancy refers to the numerical value that represents the "center" or
 "typical" observation within a dataset

central tendency are of three types...

1.mean : average value
2.median : central value
3.mode : most frequent occuring value

Note:
A). mean and median generally used for numerical columns
B). mode generally used for categorical columns

'''

# mean

'''
Note:
when mean = median then such distribution is called normally distributed data.
this distribution is also called symmetric distribution
'''

array = np.array([1,2,3,4,5,6,7,8,9,10])
mean = np.mean(array)
print(f"the mean value of the array is {mean}")
median = np.median(array)
print(f"the median value of thye array is {median}")

# Example to practice

array1 = np.array([100,400,700,300,200,100,800,900])
array1.sort()
array1
mean = np.mean(array1)
print(f"the mean value is {mean}")
median = np.median(array1)
print(f"the median value is {median}")

array1 = np.array([100,400,700,300,200,100,800,900])

max_value = np.max(array1)  # 900
min_value = np.min(array1)  # 100

range = max_value - min_value   # 900 - 100 = 800
print(f"The range of array is {range}")

# calculate variance and standard deviation
# ****** IDEAL VALUA OF STANDARD DEVAITION IS 1.
variance = np.var(array1)
print(variance)
std = np.sqrt(variance) # Square Root
print(std)

std1 = np.std(array1)
print(std1)

# calculation of IQR
import numpy as np
array1 = np.array([100,400,700,300,200,100,800,900])

Q1 = np.percentile(array1,25)
Q3 = np.percentile(array1,75)

IQR = Q3 - Q1
print(f"IQR for array1 {IQR}")

lowerwhisker = (Q1 - 1.5*IQR)
upperwhisker = (Q3 + 1.5*IQR)

print(f"The UpperWhisker Is : {upperwhisker}")
print(f"The lowerWhisker Is : {lowerwhisker}")

# lecture22

# for calculating lower and upper whisker [minimum(q1 - 1.5*IQR)] and [maximum(q3 + 1.5*IQR)]


array6 = np.arange(1,10,1)

q1 = np.percentile(array6,25)
q3 = np.percentile(array6,75)

IQR = q3 - q1
print(f"The IQR for this array is : {IQR}")

lowerwhisker = (q1 - 1.5*IQR)
upperwhisker = (q3 + 1.5*IQR)

print(f"The Upperwhisker Is : {upperwhisker}")
print(f"The lowerwhisker Is : {lowerwhisker}")

'''
the mehthods used for evaluation of outliers are as follows:
1. IQR method
2. z-test(Zscore >= 3 or Zscore <= -3 )

Note:
1. if the dataset contains outliers check the number of outliers present in the
given dataset.(Ideally the alowable percentage must be 5% )
2. if the outliers are less than 5% then we can use capping method.
3. if the outliers are more than 5% then we can use IQR method.
4. if the outliers are more than 10% then we can use z-test.
5. some people also use winsorization technique to handle outlier.
6. as far as possible avoid trimming technique.
7. if the dataset shows non-normal distribution or skewed than better to use IQR
method rather than winsorization technique.
8. if the dataset is highly skewed then use box-cox technique or yeo Jhonson
method or log normal in order to convert high skewed data into normal
distribution then only think of outlier treatment decision.
9. we may use the shapiro test to check whether the dataset is normally distributed
or not.

Note:

Z score can be evaluated as : (x - Mean)/ standard deviation)
'''

# calculate outliers using z test using scipy module

import pandas as pd
from scipy.stats import zscore


data = [5,2,4.5,3,2,6,20,9,2.5,3.5,3.75,6.5,2.5,8,1]

df = pd.DataFrame(data)
df['zscore'] = zscore(data)
df

# calculate outlier using IQR

df = np.array(data)
df

Q1 = np.percentile(df,25)
Q3 = np.percentile(df,75)

IQR = Q3 - Q1

print(IQR)

lowerwhisker = (Q1 - 1.5*IQR)
upperwhisker = (Q3 + 1.5*IQR)

print(f"The UpperWhisker Is : {upperwhisker}")
print(f"The lowerWhisker Is : {lowerwhisker}")

# Exercise:

array3 = np.array([[1,2,3,4,5,6,7,8,9,10,11,12]])
array3 = array3.ravel()

Q1 = np.percentile(array3,25)
Q3 = np.percentile(array3,75)

IQR = Q3 - Q1

print(IQR)

lowerwhisker = (Q1 - 1.5*IQR)
upperwhisker = (Q3 + 1.5*IQR)

print(f"The UpperWhisker Is : {upperwhisker}")
print(f"The lowerWhisker Is : {lowerwhisker}")

import numpy as np
array10 = np.array([1,35,6,8,3,9,4,2,0,8,4,3,8,5,36])

Q1 = np.percentile(array10,25)
Q3 = np.percentile(array10,75)

IQR = Q3 - Q1

print(IQR)

lowerwhisker = (Q1 - 1.5*IQR)
upperwhisker = (Q3 + 1.5*IQR)

print(f"The UpperWhisker Is : {upperwhisker}")
print(f"The lowerWhisker Is : {lowerwhisker}")

# Measure of Association
'''
A). covariance
B). correlation = (covariance/std)(r)

Note:

1. In order to evaluate correlation please ensure all the columns are in one scale.

2. there are three types of scaling technique
  - Standard Scaler
  - MinMix Scaler
  - Robust scaler

  Note:
  a. When the dataset is normally distributed (symmetric data) then go for
    standard scaler.
  b. When the dataset is non-normally distributed (skewed data) then go for
    minmax scaler.
  c. Whe dataset is non-normally distributed (skewed data) also containing
    lot of outliers i.e. outliers makes machine learning models sensitive
    then only go for robust scaler.

# skewness:
  skewness is classified into 3 types
  - Positive skewness
  - Negative skewness
  - Zero skewness (No skewed / symmetric distribution)

# Kurtosis:
  kurtosis is classified into 3 types :
  - Leptokutic (Heavy tailed distribution)
  - Mesokurtic (Normal distribution)
  - Platykurtic (Light tailed distribution)

# Binomial Distribution:
  - the binomial distribution is the probability distribution for the number
    of success in a sequence of Bernaolii trails

  Example:
  - person tossing a coin
      the event to occur Head : p = 0.5 i.e success
                         Tail : q = (1-p) i.e failure
                         Note : p + q = 1

 '''

from scipy.stats import binom

n,p = 10,0.5
mean , var , skew, kurt = binom.stats(n,p, moments = 'mvsk')
mean,var,skew,kurt

# binom.pmf(r,n,p)
'''
n: the total number of trails or times the experiment will be carried out.
r: a list of integers from 0 to n, inclusive.
p: the probability that the outcome of a single experiment will be a success.
the value of p must be between 0 and 1 ,inclusive.
'''

binom.pmf(1,2,0.5)

'''
Note:
- if p>0.5 then distribution is right skewed
- if p<0.5 then distribution is left skewed
- if p=0.5 then distribution is no skewness
'''

# inferential statisics are based on population
# methods : (sample size < 30) T-Test ,
# (sample size > 30)--> Z-test
