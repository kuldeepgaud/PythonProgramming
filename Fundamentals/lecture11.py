# %%

sum = 10

for i in range(1,5):
  sum = i 
  print(i + 10)

print(sum)

# %%
sum = 100

if i <=10:
  i = sum + i
  pass
  if i <=3:
    print("hii")

    if i <= 2:
      print('world')

print(sum)


# %%
def sum(num1 = 100,num2 = 200):# function definition
  num3 = num1 + num2
  print(num3)

sum() # function calling


# %%
a = 100
def sum(num3,num1 = 99,num2 = 200):  # function definition
  num4 = num1 + num2 + num3
  
  print(num4)

sum(1)  # function calling


# %%
# when the prameters are not  assigned keep the unassigned parameters at the prefix
a = 100
def sum(num3,num1 = 100,num2 = 200):  # function definition
  num4 = num1 + num2 + num3 
  
  print(num4)

sum(1,1,1)  # function calling

# %%
number1 = int(input("enter number1....: "))
number2 = int(input("enter number2....: "))

def calc(num1,num2):
  num3 = num1 + num2
  return num3

ans = calc(number1,number2)
print(ans)