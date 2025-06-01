# # single inheritance
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def eat(self):
#         print("Animal is eating")
# class Dog(Animal):
#     def bark(self):
#         print("woof")
# animal=Animal("General Animal")
# dog=Dog("Buddy")
# print(animal.name)
# animal.eat()
# print(dog.name)
# dog.eat()
# dog.bark()

# # multiple inheritance
# class Payment():
#     def make_payment(self , amount):
#         self.amount=amount
# class Paytm(Payment):
#     def make_payment(self , amount):
#         return f"paytm payment of ${amount} processed."
# class Phonepay(Payment):
#     def make_payment(self,amount):
#         return f"Phonepay amount of ${amount} processed."
# payment1 = Paytm()
# print(payment1.make_payment(100))

# payment2 = Phonepay()
# print(payment2.make_payment(500))




# # encapsulation 
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



# Recurssive case 
# class Factorial :
#     def Fact_cal(self,n):
#         if n==0 or n==1:
#             return 1
#         else:
#             return n * self.Fact_cal(n-1)
# factorial=Factorial()
# number=5
# result=factorial.Fact_cal(number)
# print(number , "is" , result)
        

