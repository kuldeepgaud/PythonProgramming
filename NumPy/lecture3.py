# CLT (central limit theorem)
'''
while writing hypothesis always use mean rather than median and mode to exclude bais.
-- sample size(n) is invertionally proportional to IQR and CI.
-- sample size is directly proportional to normal distribution
*****--higher the sample size lower the data dispersion that's why we select 10% for sample size.   

* Larger samples gives better approximation.

 '''
# standard error 
''' 
standarderror = standard deviation/ underroot of sample size(n)

** As (n) increases standarderror decreases

''' 

# solving one sample t-test using scipy module
from scipy.stats import ttest_1samp
import numpy as np

# sample = 12
marks = np.array([8,9,8,8,8,8,8,8,8,8,8.5,8])
mean = np.mean(marks)

''' 
Ho = The mean avg marks score by learners = 8
Ha = The mean avg marks score by learners != 8

'''
t_statistic,p_value = ttest_1samp(marks,8)
print(f'the p value of marks is : {p_value}')

if p_value < 0.05:
  print('Reject the null hypothesis')
else:
  print('Accept the null hypothesis')


'''
A client claim that the consignment is faulty as the standard pH value of the product
is not equal to 7. So prepare inferetial stats report to support the claim.

test_report = [7,7.1,7.2,7,7,7,7,7,8,8,9,10,7.2,9,7.2,7,7,7,7]

'''

# sample size = 19
n = 19
test_report = [7,7.1,7.2,7,7,7,7,7,8,8,9,10,7.2,9,7.2,7,7,7,7]
mean = np.mean(test_report) # ans = 7

t_statistic,p_value = ttest_1samp(test_report,7)
print(f" the p_value of the test_report is : {p_value}")

if p_value < 0.05:
  print('Reject the null hypothesis i.e Accept the alternative hypothesis')
else:
  print('Accept the null hypothesis i.e Reject the alternative hypothesis')

std = np.std(test_report)


se = std / np.sqrt(n)

print("Sample Standard Deviation:", std)
print("Standard Error:", se)

upper_bound = 7 + se
lower_bound = 7 - se

print(f"lower bound is : {lower_bound}")
print(f"upper bound is : {upper_bound}")


# Z - test

'''
Z = (x - u)/(std(sigma)/underoot of sample size(n))

x = value(sample mean)
meu (u) = mean of population
std(sigma) = std of population
n = sample size
(standard normal = mean = 0 and std = 1)

 '''

# t - TEST

'''
 T = (x - u)/(std(S)/underoot of sample size(n))

x = value(sample mean)
meu (u) = mean of population
std(sigma) = std of population
n = sample size
(standard normal = mean = 0 and std = 1)

'''


'''
MEDICINE JALRA M50 500MG(metaformin)

Client claims that metaformin content != 500mg

Ho = 500mg
Ha != 500mg


'''
from scipy.stats import ttest_1samp
import numpy as np

sample = [500,500,501,502,500,503,510,522,530,540,501,500,500,501,502,503,504]
mean = np.mean(sample)
print(f"mean of sample : {mean}")

t_statistic,p_value = ttest_1samp(sample,500)
print(f'the p value of marks is : {p_value}')

if p_value < 0.05:
  print('Reject the null hypothesis i.e accept the alternate hypothesis')
else:
  print('Accept the null hypothesis i.e reject the alternate hypothesis')


# Two sample t test using scipy module 
kuldeep = [500,501,500,500,500,501,502,506,501,500,500,500,501,500,500]
sanskruti = [500,501,500,500,500,500,500,501,501,500,500,500,500,500,500]

kuldeep_sampletest = np.array(kuldeep)
sanskruti_sampletest = np.array(sanskruti)

from scipy.stats import ttest_ind

t_test,p_value= ttest_ind(kuldeep_sampletest,sanskruti_sampletest)
print(f"the p_value of test report : {p_value}")

if p_value < 0.05:
  print("Reject Ho")
else:
  print("Accept Ho")