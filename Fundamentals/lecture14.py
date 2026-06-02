# single level inheritance

# %%
class kuldeep:

# define constructor
  def __init__(self):
    pass
# define method for parent class
  def details(self):
    pass


class zounisha(kuldeep):

# define constructor
  def __init__(self):
    pass
    super().__init__(self)    # to fetch instance variable of parent class
    pass

# define object

obj1 = kuldeep()
obj2 = zounisha()


# %%

# multi level inheritance

class kuldeep:

# define constructor
  def __init__(self):
    pass

    
# define method for parent class
  def details(self):
    pass

class zounisha(kuldeep):

# define constructor
  def __init__(self):
    pass
    super().__init__(self)    # to fetch instance variable of parent class
    pass

class sakurr(zounisha):

# define constructor
  def __init__(self):
    pass
    super().__init__(self)    # to fetch instance variable of parent class
    pass



# define object

obj1 = kuldeep()
obj2 = zounisha()
obj3 = sakurr()

# %%
# data Encapsulation(__)

''' a python encapsulation is a key concept in OOP it involves restricting the direct access to some part of an object typically
by hiding internal state and requirement and interaction through well-defined methods '''

# defining class
class employee:

  def __init__(self,
               name,
               age,
               position,
               monthly_salary):
    self.name = name
    self.age = age 
    self.__position = position
    self.__monthly_salary = monthly_salary

  def get_position(self):
    return self.__position
  def set_position(self,position):
    self.__position = position

  def get_monthly_salary(self):
    return self.__monthly_salary
  def set_monthly_salary(self,salary):
    self.__monthly_salary = salary 

  def __calculate_annual_salary(self):
    return self.__monthly_salary * 12

  def get_annual_salary(self):
    return self.__calculate_annual_salary()

  def display_employee_details(self):
    print(f"Name: {self.name}") 
    print(f"Age: {self.age}")
    print(f"Position: {self.__position}")
    print(f"monthly_salary: {self.__monthly_salary}")
    
    
emp1 = employee("Kuldeep",21,"Developer",3000000000)
emp2 = employee("shanaya",21,"Developer",3000000000) 


emp1.display_employee_details()
emp2.display_employee_details()

print(emp1.age)
print(emp2.name)







