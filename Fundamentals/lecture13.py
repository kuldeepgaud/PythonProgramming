# %%

# class definition

class bank:

  name_of_bank = "Bank of spain"


  # define constructor
  def __init__(self,
               variable1,
               variable2,
               variable3):
    self.variable1 = variable1  # instance variable1 [instance variable is accesible to any function]
    self.variable2 = variable2  # instance variable2
    self.variable3 = variable3  # instance variable3

  # methods/functions
  def method1(self):            # method1
    return self.variable1       # method variable is only accessible to only method method function

  def method2(self):            # method2
    return self.variable2

  def method3(self):            # method3
    pass

  def method4(self):            # method4
    pass


    #define object : class bank

obj1 = bank(100,200,300)

print(obj1.variable2)     # using dot operator to call instance variable2
print(bank.name_of_bank)  # using dot operator to call class variable
a = obj1.method1()
b = obj1.method2()
print(a)                  # using dot operator to call method1
print(b)


# %%

# WAP to credit and withdraw fund from bank account

class bank:

  def __init__(self,
               balance):
    self.balance = balance    # instance variable


  def withdraw(self,
               amount):
    self.amount = amount

    if self.amount <= self.balance:
      self.balance -= self.amount     # self.balance = self.balance - self.amount

      print(f"{self.amount} Debited successfully")

    else:
      print("insufficient balance")



  def deposit(self,
              amount):
    self.amount = amount
    self.balance += self.amount
    print(f"{self.amount} Credited successfully")

  def check_balance(self):
    print(f"Available Balance : {self.balance}")

obj1 = bank(10000)
obj1.withdraw(2000)
obj1.check_balance()
obj1.deposit(5000)
print(obj1.balance)


# %%

# inheritance

class animal:   # parent class

  def __init__(self,leg,eyes,ears,tail):
    self.leg = leg        # instance variable : parent class
    self.eyes = eyes      # instance variable : parent class
    self.ears = ears      # instance variable : parent class
    self.tail = tail      # instance variable : parent class

class dog(animal):    # child class

  def __init__(self,hieght,size):
    super().__init_(leg,eyes,ears,tail)
    self.hieght = hieght      # class variable
    self.size = size          # class variable

class cat(animal):    # child class

  def __init__(self,hieght,size):
    super().__init__(leg,eyes,ears,tail)
    self.hieght = hieght
    self.size = size


# %%

class bank:

  def __init__(self,name,age,gender,acc_no):
    self.name = name
    self.age = age
    self.gender = gender
    self.acc_no = acc_no


class savings_acc(bank):

  def __init__(self,intrest_rate):
    super().__init__(name,age,gender,acc_no)
    self.intrest_rate = 0.06



class current_acc(bank):

  def __init__(self,intrest_rate):
    super().__init__(name,age,gender,acc_no)
    self.intrest_rate = 0.09


class nri_acc(bank):

  def __init__(self,country):
    super().__init__(name,age,gender,acc_no)
    self.country = country

obj1 = bank("kuldeep",21,"male",123456789)
obj2 = bank("shanaya",21,"female",123456789)
print(obj1.name)
print(obj1.gender)
print(obj1.age)
print(obj1.acc_no)
print(obj2.name)
print(obj2.gender)
print(obj2.age)
print(obj2.acc_no)
