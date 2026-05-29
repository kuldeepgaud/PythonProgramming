# Concept of OOP

''' 
1.class : it is a blueprint or template of object.
2.object : it is instance(small part) of class.
3.(.operator) is responsible for fetching data.
4.__init__ (constructor) it makes variables global (special method) it binds all the files together as a package.

'''
# %%
class employee:

# defining special method
  def __init__(self,name,age,designation):
    self.name = name
    self.age = age
    self.designation = designation

emp1 = employee("kuldeep",21,"HR")
emp2 = employee("shanaya",21,"DA")

print(emp1.name)
print(emp2.name)
print(emp1.age)


# %%

# Task 1

''' 
1.define the class first : itv
2.objects to define :name,age,course,duration(in months)

'''
class itv:

  # defining special method
  def __init__(self,
               name,
               age,
               course,
               duration):
    self.name = name
    self.age = age
    self.course = course
    self.duration = duration

# defining objects

stu1 = itv('kuldeep',21,'DSDA',6)
stu2 = itv('mayur',22,'JS',3)
stu3 = itv('kashish',21,'SQL',1)
stu4 = itv('shanaya',21,'DSDA',6)

print(stu1.name)
print(stu2.age)
print(stu3.course)
print(stu4.duration)



# %%

# Task 2

''' 
1.define class = car
2.define variables in constructor = wheel,capacity,color,model
'''
class car:

  # defining special function
  def __init__(self,
               model,
               capacity,
               color,
               wheel):
    self.model = model      # instance variable / speical variable
    self.capacity = capacity
    self.color = color
    self.wheel = wheel


  # defining basic method
  def diesel_mileage(self):
    mileage = 15          # class variable
    return mileage

  def petrol_mileage(self):
    mileage = 10
    return mileage

batmobile = car('petrol',2,'frosty black',3)
tarzan = car('diesel',2,'soothing purple',4)

print(batmobile.color)
print(tarzan.capacity)


p = batmobile.petrol_mileage()
print(p)



# %%

# Design a template for bank application
''' 
1.define class first (bank)
2.define subclass (savings_acc, current_acc, nri_acc)
3.define special function (constructor)
4.define attributes inside constructor ()
'''

class bank:

  def __init__(self,
               name,
               age,
               acc_type,
               acc_no,
               passcode):
    self.name = name
    self.age = age
    self.acc_type = acc_type
    self.acc_no = acc_no
    self.passcode = passcode
    pass

  def deposit(self,
              amount):
    pass

  def withdrawal(self,
                 amount):
    pass

class savings_acc:

  def __init__(self,
               name,
               age,
               acc_no,
               passcode,
               intrest_rate):
    self.name = name
    self.age = age
    self.acc_no = acc_no
    self.passcode = passcode
    self.intrest_rate = intrest_rate

    pass


class current_acc:

  def __init__(self,
               name,
               age,
               acc_no,
               passcode):
    self.name = name
    self.age = age
    self.acc_no = acc_no
    self.passcode = passcode
    pass

class nri_acc:

  def __init__(self,
               name,
               age,
               acc_no,
               passcode,
               country):
    self.name = name
    self.age = age
    self.acc_no = acc_no
    self.passcode = passcode
    self.country = country
    pass

