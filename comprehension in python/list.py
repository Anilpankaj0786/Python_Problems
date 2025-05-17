# list comprenshion 
# list comp in python provide a concise way to create lists
# they are more readable and efficient than tradition for loops.
# syntax:
# [expression for item in iterable if condition]


# create a list of square
squares=[x**2 for x in range(1,6)]
print(squares)



# filter even number
even=[x for x in range(10) if x%2==0]
print(even)



# convert string to uppercase
names=["sam","rohit","anil"]
uppercase=[name.upper()for name in names]
print(uppercase)


# flatten a nested list
matrix=[[1,2],[3,4],[5,6]]
flattened=[num for sublist in matrix for num in sublist]
print(flattened)



# generate a list of tuple 
pairs=[(x,y)for x in range(3)for y in range(2)]
print(pairs)


