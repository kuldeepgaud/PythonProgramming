# %%
i = 0

while i < 4:
  print(i)
  i = i + 1

# %%
i = 0
while i < 4:
  print(i)
  if i == 1:
    print("Hello")
  i = i + 1

# %%
  i = 0
while i <= 5:
  if i == 1:
    print("Hello")
    if i == 2:
      print("World")

      i = i +1

  print(i)

  #%%
  i = 0

while i == 0 and i < 5:
  print(i)
  if i == 2:
    print("you win")
    i += 1.    #i = i + 1

  i = i + 1

  print(i)

# %%

i = 0

while i == 0 or i < 5:
  print(i)
  if i == 2:
    print("you win")
    i += 1.    #i = i + 1

  i = i + 1

  print(i)

# %%

# Mathematical operators in Python Programming

num = 100
num1 = 20

print(num + num1)
print(num - num1)
print(num * num1)
print(num / num1)     # 5.0 : Decimal Format (Division)
print(num // num1)    # 5   : Intergar Format (Division)
print(num % num1)
print(num ** num1)    # 2**2 = 4 Power Function

# %%

# Calculator Code

name = input("Enter your name :")
passcode = input("Enter the passcode:")

if name.lower() == "kuldeep" and passcode == "1234":

  # Calculator Programming

  number1 = float(input("Enter first number :"))
  number2 = float(input("Enter second number :"))

  Operations = input("Enter the mathematical operation to be performed")

  if Operations == '+':
    print(number1 + number2)

  elif Operations == '-':
    print(number1 - number2)

  elif Operations == '*':
    print(number1 * number2)

  elif Operations == '/':
    print(number1 / number2)

  elif Operations == '**':
    print(number1 ** number2)

  else:
    print("Invalid value , Enter the correct operations....")

# %%
