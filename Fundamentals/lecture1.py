# Single line Comment
'''
Multi line comment
1.kuldeep
2.kumar
3.gaud
'''
"""
Question: Ask User to enter two numbers and do the addition of two numbers

Logic:
1.I will ask user to enter two numbers
2.tweo numbers will be assigned to two variables
3. one variable : ans = variable1 + vairable2
4.I will print the answer

Execution:

1.input() : will take user input as string and return it back to caller function (main) as a string type value data object
2.Assign two variables with input():
variable1 = int(input()) : here we are converting the user input into interger number (int()) so that we 
3. Assign Variable : ans : variable1 + variable2
4. 
"""

# %%
# Ask the user to enter two numbers
variable1 = int(input("Enter the first number:"))
variable2 = int(input("Enter the second number"))

ans = variable1 + variable2

print(ans)

print(type(ans))

name = input("Enter the Name : ")

print(type(name))

data = float(input("enter number:"))
data2 = float(input("enter number2:"))


tdata = data + data2 

print(tdata)

print(type(tdata))


# Data Types of pythonprogramming
'''
1.Integar
2.Float
3.String
4.Boolean
5.List
6.Tuple
7.Set
8.Dictionary
'''
pi = 3.421

# note : string must be inside a quotes
name = 'India'

# Multi variable assignment are allowed
India,kuwait,America = 100,20.21,'usaa'

# The boolean is always assignmed in camelcasing
a = True
b = False

print(a and b)

