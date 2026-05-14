# concept of print function

# f - string 

# %%
name = 'KULDEEP'
AGE = 21
salary = 3000000

print(f'hii my name is {name} and my age is {AGE} and my salary is {salary}')
# %%
 
# concept of .format method 

print('hii my name is {} and my age is {} and my salary is {}'.format(name,AGE,salary))

# Concept of List 

Lst1 = []
Lst2 = [1,2,33.3,'hii','world',True,False,[10,20,30],[100,200,300],{1,2,3},{"India":1000},None]

# Control Flow 

# if condition 
# %%
name = input("Enter your name :")

if name == "kuldeep":
    print(f'Your Name is {name}')


# %%

coin_side = input("Enter the coin side:")

if coin_side.lower == "head":
    print("you have won")

if coin_side.lower == "tail":
    print("I have won")
else:
    print("Enter correct value")


# %%

coin_side = input("Enter the coin side:")

if coin_side == "head":
    print("you have won")

elif coin_side == "tail":
    print("i win")
else:
    print("Enter correct coin side")

# %%

# Concept of Indexing and slicing 

str = "Welcome to the world of python programming"
str1 = "hello world"
print(str1[6])
# %%

# str[start:stop:step]

print(str1[::3])
# %%


'''
Question : write a program to print whether the value entered by user is pallendrom or not

Logic: 
1.Ask the user to enter the string
2.Reverse the string
3.compare the original string with the reversed string
4.if both are the same then it is palindrome otherwise not a palindrome

'''
# %%
string = input("Enter a string:")
string1 = string[::-1]  #str1[start:stop:step]  : --> -1 means reverse the string

if string == string1:
    print(f"{string} is a palindrome")

else:
    print(f"{string} is not a palindrome")
# %%

