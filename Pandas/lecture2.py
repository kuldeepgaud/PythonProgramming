
# import Data manipulation library

import numpy as np
import pandas as pd

# Import Data visulization library

import matplotlib.pyplot as plt
import seaborn as sns

# Data Ingestion

def data_ingestion(data):
  df = pd.read_csv(data)
  return df

def dataset_information(df):
  info = df.info()
  duplicated_values = df.duplicated().sum()
  null_values = df.isnull().sum()
  return info, duplicated_values,null_values

# Define entry point

def main():   # function defnition
  filepath = '/content/titanic_dataset.csv'
  df = data_ingestion(filepath)   # function calling
  report = descriptive_stats(df)
  info,duplicated_values,null_values = dataset_information(df)


main()  # function calling

# step 2 : Descriptive stats : (numerical)


def descriptive_stats(df):
  from collections import OrderedDict

  stats = []

  for i in df.select_dtypes(exclude = 'object'):
    numerical_stats = OrderedDict({
        'feature': i,
        'count' :df[i].count(),
        'maximum':df[i].max(),
        'minimum':df[i].min(),
        'mean' :df[i].mean(),
        'median':df[i].median(),
        'Q1' : df[i].quantile(0.25),
        'Q3' : df[i].quantile(0.75),
        'IQR' : df[i].quantile(0.75) - df[i].quantile(0.75),
        'LW' : df[i].quantile(0.25) - 1.5*df[i].quantile(0.75) - df[i].quantile(0.75),
        'UW' : df[i].quantile(0.25) + 1.5*df[i].quantile(0.75) - df[i].quantile(0.75),
        'skew' :df[i].skew(),
        'kurt': df[i].kurt(),
        'std' : df[i].std()
    })
    stats.append(numerical_stats)
    report = pd.DataFrame(stats)
  return report

def crosstab(df):
  pd.crosstab(index = df['Sex'],columns = [df['Survived'],df['Pclass']],margins= True)
  return crosstab

# lecture5

# datetime conversion
# best to analyse stock dataset

# df['JoiningDate'] = pd.to_datetime(df['JoiningDate'],errors='coerce')

from scipy.stats import ttest_1samp
import numpy as np

def test():
  med = np.array([48,49,50,52,53,53,54,51,50,49])

  mean = np.mean(med)
  print(f"mean of med : {mean}")


  t_statistic,p_value = ttest_1samp(med,50)
  print(f'the p_value of med is {p_value}')

  if p_value < 0.05:
    print('Reject the null hypothesis i.e accept the alternate hypothesis')
  else:
    print('Accept the null hypothesis i.e reject the alternate hypothesis')

test()

# lecture6

# Import data manipulation library
import numpy as np
import pandas as pd

# Import Data visualization library
import matplotlib.pyplot as plt
import seaborn as sns

# df = pd.read_csv('/content/titanic_dataset.csv')
# df.head()

df = pd.read_csv('/content/titles.csv')
df.head()

plt.bar(df['Embarked'],df['Pclass'],color = 'gray')
plt.title('Bar Plot')
plt.xlabel('Embarked')
survived count
Pclass

plt.ylabel('class')
plt.show()

sns.barplot(data =df,x = 'Embarked',y = 'Pclass',color = 'gray')
plt.show()

year = [2000,2001,2002,2003,2004,2005]
sales_q1 = [10000,20000,40000,60000,80000,90000]
sales_q2 = [12000,8000,90000,62000,82000,92000]

# plotting box plot using seaborn library
sns.boxplot(data = sales_q1)

sns.boxenplot(data = sales_q1)

# mostly german clients ask for it
sns.violinplot(data = sales_q1 ,color = 'lightpink')
plt.show()

sns.lineplot(x = sales_q1,y = sales_q2,linestyle = '--',
             marker = 'D')

plt.show()

sns.scatterplot(x = sales_q1, y =sales_q2)
plt.grid()
plt.show()

sns.relplot(x = sales_q1,y = sales_q2)
plt.grid()
plt.show()

sns.regplot(x = sales_q1, y =sales_q2)
plt.show()

sns.jointplot(x = sales_q1,y = sales_q2)
plt.show()

plt.figure(figsize = (12,12))
plt.subplots(2,2)
plt.subplot(2,2,1)
plt.plot(year,sales_q1)
plt.subplot(2,2,2)
plt.plot(year,sales_q2)
plt.subplot(2,2,3)
sns.boxplot(data = sales_q1)
plt.subplot(2,2,4)
sns.boxplot(data = sales_q2)
plt.show()