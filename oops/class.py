# class Employee:
#     location = "jaipur"
    
#     def __init__(self,name,jobrole):
#         self.name = name
#         self.jobrole = jobrole
#     def getInfo(self):
#         print(f"Name of Employee is : {self.name} and jobrole is : {self.jobrole}")
# e = Employee('sam','Frontend Developer')
# e.getInfo()
# a = Employee('Rahul','MLOPS')
# a.getInfo()
# Employee.location





# ### Create a calculator Class
# class Calculator:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#     def add(self):
#         return self.num1 + self.num2
#     def subtract(self):
#         return self.num1 - self.num2
#     def multiply(self):
#         return self.num1 * self.num2
#     def divide(self):
#         if(self.num2 != 0):
#             return self.num1/self.num2
#         else:
#             return "Divide by zero is not allowed!"
            
# calc = Calculator(10,5)
# print(calc.add())
# print(calc.subtract())
# print(calc.multiply())
# print(calc.divide())




# ### Create a Bank Account Class 
# class BankAccount:
#     def __init__(self,holder_name,balance = 0):
#         self.holder_name = holder_name 
#         self.balance = balance
#     def deposit(self , amount):
#         self.balance += amount
#         print(f"{amount} deposited. New balance : {self.balance}")
#     def withdraw(self , amount):
#         if amount <= self.balance:
#             self.balance -= amount ## self.balance = self.balance - amount
#             print(f"{amount} withdrawn. Remaining balance : {self.balance}")
#         else:
#             print("Insufficient funds!")
#     def check_balance(self):
#         return f"Account balance for {self.holder_name}: {self.balance}"
# #Test the Bank Account class
# account = BankAccount("Saurabh",1000)
# account.deposit(500)
# account.withdraw(300)
# print(account.check_balance())



# ### Create a Student Class
# class Student:
#     def __init__(self,name,age,marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
        
#     def display_details(self):
#         print(f"Name : {self.name} , Age: {self.age} , Marks: {self.marks}")
    
#     def has_passed(self):
#         if self.marks >= 40:
#             return "Passed"
#         else:
#             return "Failed"

# student = Student("Riya",20,85)
# student.display_details()
# print(student.has_passed())




# class BankAccount:
#     def __init__(self, holder_name, balance=0):
#         self.holder_name=holder_name
#         self.balance=balance
#     def deposit(self, amount):
#         self.balance+=amount
#         print( f"{amount} deposited to your account:{self.balance}")
#     def withdraw(self, amount):
#         if amount<=self.balance:
#             self.balance-=amount
#             print(f"{amount} withdraw amount,total:{self.balance}")
#         else:
#             print("insufficiant fund")
#     def checkbalance(self):
#           return f"Account balance for {self.holder_name}: {self.balance}"

# account=BankAccount("Anil",1000)
# account.deposit(500)
# account.withdraw(300)
# print(account.checkbalance())





# class BankAccount:
#     def __init__(self, holder_name, balance=0,min_balance=5000):
#         self.holder_name=holder_name
#         self.balance=balance
#         self.min_balance=min_balance
#     def deposit(self, amount):
#         self.balance+=amount
#         print( f"{amount} deposited to your account:{self.balance}")
#     def withdraw(self, amount):
#         if self.balance-amount>=self.min_balance:
#             self.balance-=amount
#             print(f"{amount} withdraw amount,total:{self.balance}")
#         else:
#             print(f"Withdrawal denied. Minimum balance of {self.min_balance} must be maintained!")
#     def checkbalance(self):
#           return f"Account balance for {self.holder_name}: {self.balance}"

# account=BankAccount("Anil",10000)
# account.deposit(500)
# account.withdraw(300)
# print(account.checkbalance())



# class Student:
#     def __init__(self,name):
#         self.name=name
#         # self.score=score
#         self.__score=[]
       
#     def get_score(self):
#         return self.__score
#     def set_score(self , new_score):
#         if 0 <= new_score <= 100:
#             # self.__score = new_score
#             self.__score.append(new_score)
#             return f"new_score {new_score} added for {self.name}"
#     def get_average_score(self):
#         if len(self.__score) == 0:
#             return "No scores available to calculate the average."
#         return sum(self.__score) / len(self.__score)
#     # def get_score(self):
#     #     return self.__score
# student= Student("Anil")
# print(student.set_score(20))
# print(student.set_score(30))
# print(student.get_score())
# print(student.get_average_score())



# # Exercise 3: Build a class Employee with multiple constructors that can initialize an employee object in different ways.
# class Employee:
#     def __init__(self,name,id=None,department=None):
#         self.name=name
#         self.id=id
#         self.department=department
#     def get_name(self):
#         return self.name
#     def get_id(self):
#           return self.id
#     def get_department(self):
#           print(f"Department: {self.department}")
# employee=Employee("Anil",id=123,department="cse")
# print(employee.get_name())
# print(employee.get_id())
# print(employee.get_department())






