# Lambda Function  ==> A lambda function can take any number of arguments  but can only have one expression .
# syntax : lambda arguments : expression
# Ex.1
x = lambda a : a + 5
# print("Total value = " , x(2))

# # Ex.2
x = lambda a,b : a*b
# print("Total product is =" , x(3,4))

# # Ex.3

x = lambda a,b,c : a+b-c
print("Total=" , x(4,5,6))







# Filter Function ==> The filter function returns an iterator where the items are filtered through a
# function to test  , if the item is accepted return true or false .

ages = [5,12,17,18,34,67,50]
def myFunc(x):
    if (x<=18) :
        return True
    else :
        return False

kid = list(filter(myFunc , ages))
print(kid)






# Map Function()  ==> The map() executes a specified function for each item in a iterable.
# The item is sent to the function as parameters.

a = ["3" , "45" , "89"]

# # method -1
print(a)
# for i in range(len(a)):
#     a[i] = int(a[i])
# print(a)


# method -2 (by using map function)
b = list(map(int , a))
print(b)




a  = [1,2,3,4]
print(a)
def my_squ(a):
  return a**2

b = list(map(my_squ , a))
print(b)