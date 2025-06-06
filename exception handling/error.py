# Exceptional Handling 
# try  ---> Write our logic or program 

# except  ----> if the programs fails then it will return statement . 


# try : 
#     a = 5 
#     b = a/0
#     print(b) 
# except Exception as e : 
#     print("You cannot divide characters and zero...." , e)



# # Example 2: Handling ValueError
# try:
#         number = int(input("Enter number:")) 
#         print(number)
# except ValueError as e:
#         print("You cannot enter characters only pass integers:", e)


# # Example 3: Handling KeyError
# try:
#         data = {"name": "Alice" , "subject":"maths"}
#         print(data["roll"])  
# except KeyError as e:
#         print("Caught a KeyError:", e)


# # Example 4: Handling IndexError
# try:
#         my_list = [1, 2, 3]
#         print(my_list[8])  
# except IndexError as e:
#         print("Caught an IndexError:", e)



#  # Example 5: Handling FileNotFoundError
# try:
#         with open("non_existent_file.txt") as file:
#             content = file.read()
# except FileNotFoundError as e:
#         print("Caught a FileNotFoundError:", e)

