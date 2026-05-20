# Lecture5 below

# Concept of pass, continue and break

# %%
for i in range(1,5):
  print(i, end = " ")


# %%
for i in range(1,5):
  print(i, end = " ")     #end function gives the horizontal output
  break                   # break will break the loop and will not enter in loop


# %%
for i in range(0,21,2):
  print(i , end = " ")

# %%
for i in range(1,5):
  print(i,end = " ")
  continue              # continue function will skip the value after the loop 


# %%
for i in range(1,5):
  pass                  # pass function will not through an error even if nothing is written in the loop


# %%
for i in range(1,5):
  continue              # it will not give any output becoz it skips the loop   
  print(i)


# %%
for i in range(1,5):
  print(i,end = " ")
  continue


 # %% 
for i in range(1,8):
  if i % 2 == 0:
    print(i)
    pass


  continue

# %%
i = 0 

while i <= 5:
  for i in range(1,5):
    pass
    print(i)
    i += 1
  break

# %%
i = 0 

while i <= 5:
  for i in range(1,5):
    pass
    print(i)
    i += 1
    break
  
# %%
i = 0 
while i <= 5:
  for i in range(1,5):
    i = i + 1
    print(i)  
  break
  i = i + 1
  continue


'''
logic:

1. ask user to enter name,passcode,acct_no,withdraw_amt,acct_type
2. defined variables: saving_acct = 10000 and current_acct = 2000
3. condition: type == 1 for saving_acct and type == 2 for current_acct
4. if withdraw_amt <= saving_acct : balance  = saving_acct - withdraw_amt
5. if withdraw_amt <= current_acct : balance  = current_acct - withdraw_amt
6. print(balance)

'''

# %%
# Define User Variables
name = input("Enter the Name :")
acct_no = int(input("Enter the Account Number : "))
passcode = int(input("Enter the Passcode : "))
withdraw_amt = int(input("Enter the Withdraw Amount : "))


# Define Variables
saving_acct = 10000
current_acct = 2000

# Condition: ask user to enter the type of account
'''
1: Saving Account
2: Current Account
'''
account = input("Enter the type of account (1 and 2): ")

if account == "1":
  if withdraw_amt <= saving_acct:
    balance = saving_acct - withdraw_amt
    print(balance)
  else:
    print("Insufficient Balance")

if account == "2":
  if withdraw_amt <= current_acct:
    balance = current_acct - withdraw_amt
    print(balance)
  else:
    print("Insufficient Balance")

