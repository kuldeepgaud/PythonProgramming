''' 
List : Mutable : []
Tuple : Immutable :()
Set : Mutable : {}
Dictionary : Mutable : {}

'''

d = {1,2,3}

print(type(d))

# %%

"A parenthesis bracket doesn't contain any value it's type will be defined as Dictionary"
e = {}
print(type(e))

# %%
# d = {'Key' : value}

d1 = {'India' : 1000, 'USA' : 3000 ,'Uk' : 4000}
print(d1.keys())  #India , USA , Uk

# %%
# In dictionary keys must be unique 

d1 = {'India' : 1, 'India' : 3 ,'Uk' : 4000}
print(d1.keys())  #India , USA , Uk

# %%
# in case of same keys python always consider the recently assigned value
d1.values()

# %%
d1.items()

# %%
# pop will remove the specified argument
d1.pop('Uk')

# %%
# popitem removes the key : value at suffix
d1.popitem()

# %%
d2 = {'name' : 'kuldeep',
      'age' : 21,
      'gender' : 'male'}

d2.popitem()

print(d2)

# %%
# .get will retrieve the defined keys value
d2.get('name')

# %%
d2.update({'name' : 'H2'})
d2.update({'Age' : 33})
d2


# %%
d2.pop('Age')

# %%
d2

# %%
# Expected Output {'name': 'kuldeep', 'age': 42}
d2['name'] = 'kuldeep'
d2['age'] = 21
d2

# %%
# Function Definition : def

def hello(): # function definition
  print('Hello, How are you...')

hello() # function calling


# %%
def greet(): # function definition
  pass

greet()      # function calling

# %%
# write a function to check whether the given string is pallindrom 

string = input("Enter the string ...")
string1 = string[::-1]

def pallindrom():

  if string == string:
    print("String is pallindrom")
  else:
    print("String is not a pallindrom")

pallindrom()


# %%
# write a function to create a calculator 

''' 
Logic:
1.i will ask the user to enter the two numbers
2.ask the user to enter the operator 

'''




First_number = float(input("Enter the first number"))
second_number = float(input("Enter the second number"))

operation = input("Enter the mathematical operation...")

def calculator():
  if operation == "+":
    print(First_number + second_number)

  elif operation == "-":
    print(First_number - second_number)

  elif operation == "*":
    print(First_number * second_number)

  elif operation == "/":
    print(First_number / second_number)

  else:
    print("invalid input")

calculator() 


# %%
# ask the user to enter the strings and count the number of vowels in the string

''' 
Logic:
1. Ask the user to enter a string
2. check the string if string == vowels(a,e,i,o,u)



'''

# Function to count vowels in a string

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

# Ask the user to enter a string
string = input("Enter a string: ")

# Call the function and display result
result = count_vowels(string)

print("Number of vowels:", result)



