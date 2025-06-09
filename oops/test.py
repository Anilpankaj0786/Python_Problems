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
        

# 1. Remove duplicates from a list without using set.
# list=[1,2,3,4,5,5,4,]
# x=[]
# for i in list:
#     if i not in x:
#         x.append(i)
# print(x) 
        
# 2. Write a function that flattens a nested list (e.g., [[1,2],[3,[4,5]],6] → [1,2,3,4,5,6]).
# def flatten_list(lst):
#     result = []
#     for i in lst:
#         if isinstance(i, list):
#             result.extend(flatten_list(i))
#         else:
#             result.append(i)
#     return result
# nested_list = [1, [2, [3, 4], 5], [6, 7], 8]
# flattened = flatten_list(nested_list)
# print("Flattened list:", flattened)


# 3. Rotate a list to the right by k steps (e.g., [1,2,3,4,5], k=2 → [4,5,1,2,3]).
# def rotate_list(lst, k):
#     k = k % len(lst)
#     return lst[-k:] + lst[:-k] 
# numbers = [1, 2, 3, 4, 5]
# rotated = rotate_list(numbers, 2)
# print(rotated)


# 4. Find all pairs in a list whose sum is equal to a target number.
# def find_pairs(lst, target):
#     result = []
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if lst[i] + lst[j] == target:
#                 result.append((lst[i], lst[j]))
#     return result
# numbers = [1, 2, 3, 4, 5, 6]
# target_sum = 7
# pairs = find_pairs(numbers, target_sum)
# print("Pairs that sum to", target_sum, ":", pairs)

#5. Given a list of tuples like [('a',1), ('b',2), ('a',3)], write a function to group values by key into a dictionary.
# def group_by_key(pairs):
#     result = {}
#     for key, value in pairs:
#         if key in result:
#             result[key].append(value)
#         else:
#             result[key] = [value]
#     return result

# pairs = [("a", 1), ("b", 2), ("a", 3), ("b", 4), ("c", 5)]
# grouped = group_by_key(pairs)
# print("Grouped by key:", grouped)


#6. Write a function that takes a list of tuples and returns a tuple with the max sum of its elements.
# def max_sum(tuples):
#  max_sum = 0
#     max_tuple = None
#     for tuple in tuples:
#         tuple_sum = sum(tuple)
#         if tuple_sum > max_sum:
#             max_sum = tuple_sum
#             max_tuple = tuple
#     return max_tuple
# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# result = max_sum(tuples)
# print(result)


  


#7. Count the frequency of each word in a sentence and return a dictionary.




#8. Merge two dictionaries. If a key appears in both, sum their values.
# def merge_dicts(dict1, dict2):
#     merged = dict1.copy()
#     for key, value in dict2.items():
#         if key in merged:
#             merged[key] += value
#         else:
#             merged[key] = value
#     return merged
# dict1 = {'a': 10, 'b': 20, 'c': 30}
# dict2 = {'b': 15, 'c': 25, 'd': 40}

# merged_dict = merge_dicts(dict1, dict2)
# print("Merged dictionary:", merged_dict)

# x={'a':1,'b':2,'c':3}
# y={'p':1,'q':2,'r':3}
# merge={}
# for key in set(x)|set(y):
#     merge[key]=x.get(key,0) + y.get (key,0)
# print(merge)


#9. Sort a dictionary by its values in descending order.
# data = {'apple': 3, 'banana': 1, 'cherry': 5, 'date': 2}
# sorted_dict = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
# print(sorted_dict)


#10. Write a function to invert a dictionary: {1: 'a', 2: 'b'} → {'a': 1, 'b': 2}.


# def invert_dict(d):
#     return {v: k for k, v in d.items()}
# d = {1: 'a', 2: 'b'}
# inverted = invert_dict(d)
# print(inverted)

#11. Use lambda and map to square each number in a list.
# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, numbers))
# print(squared)

#12. Use filter and lambda to filter out all the even numbers from a list.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums)


#13. Given a list of names, use map to convert each name to Title Case.
# names = ['john', 'jane', 'bob']
# title_case_names = list(map(lambda x: x.title(), names))
# print(title_case_names)

# 14.  Use a function with argument and parameter to find the product of all numbers in a list.
# def product(numbers):
#     result = 1
#     for num in numbers:
#         result *= num
#     return result
# numbers = [1, 2, 3, 4, 5]
# result = product(numbers)
# print(result)

#15.  Use map() and lambda to combine two lists element-wise into sums.
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# result = list(map(lambda x, y: x + y, list1, list2))
# print(result)

#16. Given a list of dictionaries [{name: "A", age: 25},...], use filter() to get only those with age > 30.
# people = [{'name': 'Anil', 'age': 25}, {'name': 'Pankaj', 'age': 30}, {'name': 'Vijay', 'age': 35}]
# result = list(filter(lambda x: x['age'] > 30, people))
# print(result)

#17. Write a function that finds the first non-repeating character in a string.
# def first_non_repeating_char(s):
#     char_count = {}
#     for char in s:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#     for char in s:
#         if char_count[char] == 1:
#             return char
#     return None
# s = "aabbcdd"
# result = first_non_repeating_char(s)
# print(result)


# 18. Create a dictionary from two lists, one of keys and one of values.
# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# result = {k: v for k, v in zip(keys, values)}
# print(result)

#19. Write a function to check if two lists are anagrams of each other.
# def are_anagrams(str1, str2):
#     return sorted(str1) == sorted(str2)
# str1 = "listen"
# str2 = "silent"
# result = are_anagrams(str1, str2)
# print(result)

#20. Implement a frequency counter using list comprehension and dictionary.
# def frequency_counter(lst):
#     return {item: lst.count(item) for item in lst}
# lst = [1, 2, 2, 3, 3, 3]
# result = frequency_counter(lst)
# print(result)




# Case Study: Sales and Inventory Management System
# Objective:
# Design a Python-based system for a retail company that manages inventory, sales, and profit tracking using Object-Oriented Programming. The company wants to:
# Add new products.
# Update stock.
# Record customer purchases.
# Automatically update inventory.
# Calculate total revenue and profit per product.

# Entities & Structure:
# Product: Represents individual items.
# Inventory: Manages the collection of products.
# SalesRecord: Logs each sale and helps compute revenue and profit.
# StoreManager: Interface to interact with all operations.

# class Product:
#     def __init__(self, name, price, cost):
#         self.name = name
#         self.price = price
#         self.cost = cost
#         self.stock = 0


# class Inventory:
#     def __init__(self):
#         self.products = {}

#     def add_product(self, product, quantity):
#         if product.name not in self.products:
#             self.products[product.name] = product
#         self.products[product.name].stock += quantity

#     def update_stock(self, name, quantity):
#         if name in self.products:
#             self.products[name].stock += quantity
#         else:
#             return "Product not found"

#     def sell_product(self, name, quantity):
#         if name in self.products:
#             product = self.products[name]
#             if product.stock >= quantity:
#                 product.stock -= quantity
#                 return product.price * quantity
#             else:
#                 return "Not enough stock"
#         else:
#             return "Product not found"


# class SalesRecord:
#     def __init__(self):
#         self.sales = []  # Store tuples of (product, quantity, revenue, profit)

#     def record_sale(self, product, quantity):
#         revenue = product.price * quantity
#         profit = (product.price - product.cost) * quantity
#         self.sales.append({"product": product.name, "quantity": quantity, "revenue": revenue, "profit": profit})

#     def total_revenue(self):
#         return sum(sale["revenue"] for sale in self.sales)

#     def total_profit(self):
#         return sum(sale["profit"] for sale in self.sales)


# class StoreManager:
#     def __init__(self):
#         self.inventory = Inventory()
#         self.sales_record = SalesRecord()

#     def add_product(self, name, price, cost, quantity):
#         product = Product(name, price, cost)
#         self.inventory.add_product(product, quantity)

#     def purchase(self, name, quantity):
#         if name in self.inventory.products:
#             product = self.inventory.products[name]
#             if product.stock >= quantity:
#                 product.stock -= quantity
#                 self.sales_record.record_sale(product, quantity)
#                 print(f"Sold {quantity} of {name} for {product.price * quantity}.")
#             else:
#                 print("Not enough stock to complete the purchase.")
#         else:
#             print("Product not found.")

#     def report(self):
#         print("\nInventory Report:")
#         for product in self.inventory.products.values():
#             print(f"Product: {product.name}, Price: {product.price}, Stock: {product.stock}")

#         print("\nSales Report:")
#         print("Total Revenue:", self.sales_record.total_revenue())
#         print("Total Profit:", self.sales_record.total_profit())


# # Example Usage
# store = StoreManager()

# # Add products
# store.add_product("Laptop", 1000, 800, 10)
# store.add_product("Mouse", 50, 20, 50)

# # Make purchases
# store.purchase("Laptop", 2)
# store.purchase("Mouse", 5)

# # Display report
# store.report()