# 1. *args (Non-Keyword Arguments)
# *args allows you to pass multiple positional arguments to a function.
# It collects them into a tuple.
# example 1
def add_numbers(*args):
    total = sum(args)
    print(f"Sum: {total}")
    
add_numbers(5, 10, 15)  



# 2. **kwargs (Keyword Arguments)

# **kwargs allows you to pass multiple keyword arguments (name-value pairs).
# It collects them into a dictionary.
# example 1
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Saurabh", age=25, city="Mumbai")



# 3. Using *args and **kwargs Together

# You can use both in the same function, but *args must come before **kwargs.
# example 1
def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

display_info(1, 2, 3, name="Saurabh", age=25)




# 4. Required Arguments (Mandatory Inputs)
# These are arguments that must be passed to a function; otherwise, Python throws an error.
# There is no default value for these arguments.
# example1
def greet(name):
    print(f"Hello, {name}!")

greet("Saurabh") 
# greet()  


# 5. Default Arguments (Optional Inputs)
# These arguments have a default value assigned.
# If no value is provided, Python uses the default.
# example1
def greet(name="Guest"):
    print(f"Hello, {name}!")

# greet("Saurabh") 
greet()  



# 6. return Keyword (Output of a Function)
# The return statement sends a value back from a function.
# If return is not used, the function returns None.
# example1
def add(a, b):
    return a + b  

result = add(5, 3)
print(result)  

