# # Lambda Function  ==> A lambda function can take any number of arguments  but can only have one expression .
# # syntax : lambda arguments : expression
# # Ex.1
# x = lambda a : a + 5
# # print("Total value = " , x(2))

# # # Ex.2
# x = lambda a,b : a*b
# # print("Total product is =" , x(3,4))

# # # Ex.3

# x = lambda a,b,c : a+b-c
# print("Total=" , x(4,5,6))







# # Filter Function ==> The filter function returns an iterator where the items are filtered through a
# # function to test  , if the item is accepted return true or false .

# ages = [5,12,17,18,34,67,50]
# def myFunc(x):
#     if (x<=18) :
#         return True
#     else :
#         return False

# kid = list(filter(myFunc , ages))
# print(kid)






# # Map Function()  ==> The map() executes a specified function for each item in a iterable.
# # The item is sent to the function as parameters.

# a = ["3" , "45" , "89"]

# # # method -1
# print(a)
# # for i in range(len(a)):
# #     a[i] = int(a[i])
# # print(a)


# # method -2 (by using map function)
# b = list(map(int , a))
# print(b)




# a  = [1,2,3,4]
# print(a)
# def my_squ(a):
#   return a**2

# b = list(map(my_squ , a))
# print(b)






# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75

# x = lambda a : a * i
# for i in range(2,6):
#   print("Total value = " , x(15))



# Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

# list=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# list.sort(key=lambda x: x[1])
# print(list)



# Write a Python program to filter a list of integers using Lambda.

# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Original list of integers:")
# print(nums)
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums)
# odd_nums = list(filter(lambda x: x % 2 != 0, nums))
# print(odd_nums) 



# Write a Python program to triple all numbers in a given list of integers. Use Python map.
a=[1,2,3,4,5,]
print(a)
def triple(a):
    return a*3
b = list(map(triple , a))
print(b)



# Write a Python program to add three given lists using Python map and lambda.
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]
result = map(lambda x, y, z: x + y + z, nums1, nums2, nums3)
print(list(result))



# Write a Python program to add two given lists and find the difference between them. Use the map() function.
nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]
def addition_subtrction(x, y):
    return x + y, x - y
result = map(addition_subtrction, nums1, nums2)
print(list(result))
