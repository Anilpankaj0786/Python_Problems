# Encapsulation refers to bundling data and methods that work on the data into a single unit usually a class 
# There are 2 types of attributes:
# (1) Public attribute - accessible publicly
# (2) Private attribute - __name
# Why is Encapsulation is important?
# It is important because it improves data security by restricting unauthorised access.
# It promotes modularity by hiding implementation details.
# It enables control over the data by providing control access through methods.
# It enhances code maintainablitiy and reusability by protecting data from unintented modifications.

# Example - Bank Account
class BankAccount:
    def __init__(self,account_holder,balance = 0):
        self.__account_holder = account_holder
        self.__balance = balance
    
    #Getter for account holder
    def get_account_holder(self):
        return self.__account_holder

    # Getter for balance 
    def get_balance(self):
        return self.__balance
    
    # Method to deposit money
    def deposit(self , amount):
        self.__balance += amount
        print(f"{amount} deposited. New balance : {self.__balance}")
    
    # Method to withdraw Money   
    def withdraw(self , amount):
        if amount <= self.__balance:
            self.__balance -= amount ## self.balance = self.balance - amount
            print(f"{amount} withdrawn. Remaining balance : {self.__balance}")
        else:
            print("Insufficient funds!")
            
    def check_balance(self):
        return f"Account balance for {self.__account_holder}: {self.__balance}"

#Using the class
account = BankAccount("Sam",1000)
print(account.get_account_holder())
print(account.get_balance())
account.deposit(500)
account.withdraw(300)
print(account.check_balance())

# Attempt to access private attribute directly (not allowed)
# print(account.__balance) # Error : AttributeError


## Example 2 : Student Data
class Student:
    def __init__(self,name,grade):
        self.name = name
        self.__grade = grade
        
    # Getter the grade
    def get_grade(self):
        return self.__grade

    # Set for grade (with validation)
    def set_grade(self , new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
            return "Grade updated sucessfully!"
        else:
            return "Invalid grade! Must be between 0 and 100"

student = Student("Riya", 85)
print(student.name)
print(student.get_grade())
print(student.set_grade(55))
print(student.get_grade())

#Attempt to set an invalid grade
print(student.set_grade(150))
# Output: Invalid grade! Must be between 0 and 100



