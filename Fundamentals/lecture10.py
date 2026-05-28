#Day10:

# write a program to count vovels present  inside a string
'''
aske a user to enter a string and count the no. of vovels in string
'''


string = input("enter a string : ") #afhbgaf

def vovel ():
  b = 0
  for i in range(len(string)):
    if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u':
      b = b + 1
  print(b)

vovel()

#2nd method

string = input("enter a string : ")
vovels = "aeiouAEIOU"

def count_vovels():
  count = 0
  for i in string:
    if i in vovels:
      count += 1

  return count          # return use for not print none data type
c = count_vovels()
print(c)


# %%
def sum():
  num1 = 100
  num2 = 200

  num3 = num1 + num2
  return num3,num1,num2

ans1,ans2,ans3 = sum()
print(ans1)
print(ans2)
print(ans3)

# %%
num1 = int(input("Enter the number1 : "))        # num1 and num2 is global veriable
num2 = int(input("Enter the number2 : "))

def sum():
  num3 = num1 + num2

  return num3

def minus():
  num3 = num1 - num2

  return num3
addition = sum()
substraction = minus()
print(addition)
print(substraction)

# %%
a = int(input("Enter the number : "))
b = int(input("enter the number : "))
c = int(input("Enter the number : "))


def sum(num1,num2):
  num3 = num1 + num2

  return num3

def minus(num1,num2):
  num3 = num1 - num2

  return num3

addition = sum(a,b)
substraction = minus(b,c)
print(addition)
print(substraction)

# %%
number = int (input("enter the value : "))
'''
 print a fibonacci series less than n
'''
def fib(n):         # write fibonacci series less than n
  a,b = 0,1
  while a < n:
    print(a, end=" ")
    a, b = b, a+b
  print()

ans = fib(number)

# %%
a = {"mayur","kuldeep","riya"}
b = {"sanskruti","divyanshi","abdul"}
a.update(b)
print(a)