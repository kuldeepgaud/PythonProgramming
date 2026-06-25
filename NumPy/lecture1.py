''' 
numpy :
- It is a vectorised form of an array
- num --> Numerical and py --> python
- numpy is N-dimensional array

example:
1. a = np.array([2])    # 1D NumPy Array
1. b = np.array([[2,3]])    # 2D NumPy Array
1. c = np.array([[[2,3,4]]])    # 3D NumPy Array
'''

import numpy as np
array = np.array([1,2,3])
print(type(array))

# %%
array.ndim  # ndim : dimension of an array


# %%
print(array.shape )# shape: it shows elements arranged in an numpy array (MxN)

array1 = np.array([[1,2,3],[4,5,6]])
array1.shape

# %%
array2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array2.shape)

# %%
array2

# %%
array2.T  # Transpose of a matrix : change rows to column

# %%
# flatten() : this will convert 2D to 1D
array2.flatten()

# %%
array2.sum()

# %%
# sum the array in rows
array2.sum(axis = 1)

# %%
# sum the array columnvise
array2.sum(axis = 0)

# %%
array2.max(),array2.min(),array2.mean()

# %%
# identical matrix
np.eye(9)

# %%
np.zeros(5)

# %%
np.ones(3)

# %%
array3 = np.array([[1,2,3],[4,5,6],[5,6,7],[8,9,10]])

print(array3.shape)
array3.reshape(2,6)   # Reshape = (m,n)

# %%
# mathematical operations in array [+,-,*,/]
array4 = np.array([[1,2,3],[4,5,6],[7,8,9]])
array5 = np.array([[1,2,3],[4,5,6],[7,8,9]])

b = array4 + array5
print(b)

# %%
b = array4 - array5
print(b)

# %%
b = array4 * array5
print(b)

# %%
b = array4 / array5
print(b)

# %%
# we can also perform operations with specific number
array4 * 30

# %%
array4 > 1


# %%
# only applicable for even sets for elements like (12,14,16)
np.array([[1,2,3,4,5,6,7,8,9]]).reshape(3,3)

# %%
# concept of indexing and slicing
array4[:1,:1]

# %%
import numpy as np
d = np.array([[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]]).reshape(7,5)
d

d[4:5,3:4]


# %%
# np.arange(start,stop,step) all even numbers
d = np.arange(0,36,2)
d

# %%
# .linspace divides assigned( e.g --> 0,100) number into equal parts
d = np.linspace(0,100,6,dtype= 'int')
d

# %%
# Generating random numbers

np.random.seed(0)     # Lock the random values
np.random.rand(3,3)   # generate random matrix of (3,3)

# %%
# Generating random numbers

f = np.random.randint(low = 0,high = 2,size = (3,3))
f

# %%
# note: ravel(): it is more efficient than flatten()
f.ravel()   # ravel(): perform the same task as flatten()

# %%
# Basic stats : max, min, sum, mean, median, std, var 

''' 
1.when mean = median then the distribution is symmetric/ (normally 
 distributed or no skewed Distribution).
2. when mean > median the the distribution is positively skewed
2. when mean < median the the distribution is negatively skewed
'''

np.median(f),np.mean(f),np.std(f),np.var(f),np.max(f),np.min(f),np.sum(f)
