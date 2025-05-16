# 1. Find the Maximum Number Using *args
# 🔹 Question: Write a function that takes multiple numbers as arguments using *args and returns the maximum number.
def find_max(*args):
    return max(args)

print(find_max(10, 5, 25, 8, 100))  
print(find_max(-1, -10, -5, 0))




# 2. Calculate the Product of Numbers Using *args
# 🔹 Question: Write a function that takes multiple numbers using *args and returns their product.
def product(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(product(2, 3, 4))  
print(product(5, 5))  



# 3. Generate a Full Name Using **kwargs
# 🔹 Question: Write a function that takes a first name and last name as keyword arguments and returns the full name.
def full_name(**kwargs):
    return f"{kwargs.get('first_name', 'Unknown')} {kwargs.get('last_name', 'Mehta')}"

print(full_name(first_name="Saurabh", last_name="Sharma"))  
print(full_name(first_name="Rahul"))  


# 4. Count Vowels in a Given String Using return
# 🔹 Question: Write a function that counts the number of vowels in a string and returns the count.
def count_vowels(string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)

print(count_vowels("Hello World"))  
print(count_vowels("Python"))  


# 5. Create a Shopping Cart Using *args and **kwargs
# 🔹 Question: Write a function where *args represents the items bought, and **kwargs contains prices. Return the total bill.
def shopping_cart(*items, **prices):
    total = sum(prices[item] for item in items if item in prices)
    return total

print(shopping_cart("graphs", "banana","mango", graphs=50, banana=20, mango=30))  
print(shopping_cart("pizza", "grapes", pizza = 50 , grapes=40))  




# 6. Function with Required and Default Arguments
# 🔹 Question: Write a function that requires a name and has an optional age argument (default is 18). It should return a greeting.
def greet(name, age=18):
    return f"Hello {name}, you are {age} years old."

print(greet("Saurabh"))  
print(greet("Rahul", 25))  



# 7. Calculate Discounted Price Using **kwargs
# 🔹 Question: Write a function that takes a price and a discount percentage as keyword arguments and returns the discounted price.
def discount_price(**kwargs):
    price = kwargs.get("price", 0)
    discount = kwargs.get("discount", 0)
    return price - (price * discount / 100)

print(discount_price(price=1000, discount=10))  
print(discount_price(price=500, discount=20))  



# 8. Merge Two Lists Using *args
# 🔹 Question: Write a function that accepts two lists as *args and merges them.
def merge_lists(*args):
    return [item for lst in args for item in lst]

print(merge_lists([1, 2, 3], [4, 5, 6]))  
print(merge_lists(["a", "b"], ["c", "d"], ["e"]))  




# 9. Extract Even and Odd Numbers Using return
# 🔹 Question: Write a function that takes a list of numbers and returns two lists: one with even numbers and one with odd numbers.
def separate_even_odd(numbers):
    even = [num for num in numbers if num % 2 == 0]
    odd = [num for num in numbers if num % 2 != 0]
    return even, odd

evens, odds = separate_even_odd([1, 2, 3, 4, 5, 6])
print("Evens:", evens)  
print("Odds:", odds)  


# 2 method
a = [1,2,3,4,5]
b = []
c = []
for i in range(len(a)):
    if(a[i]%2==0):
        b.append(a[i])
    else:
        c.append(a[i])
print(b)
print(c)
