# Introduction to Numpy -----> 
# Numpy is an open-source library that is used for scintific calculations .


# How Numpy is btter than List ? 
# (1). Numpy is homogeneous  data type while list is hetrogenous data type . 
# (2). Numpy takes less memory while list take more memory . 
# (3). Numpy take less execution time while List take more execution time . 

# pip install numpy 

# import numpy as np 

# a = [1,45,78,90]
# type(a) 
# b = np.array(a)
# print(b)

# a = [] 
# size = int(input("Enter size:"))
# for i in range(size):
#     val = int(input("Enter element:"))
#     a.append(val) 
# # print(a) 
# b = np.array(a) 
# print(b)



# type(b) 


# a = [[1,2,3,4],[4,5,6,7],[7,8,9,5]]
# print(a)



# b = np.array(a) 
# print(b)



# print("Total Rows and columns:" , b.shape)  ## shape = n(rows) , n(columns)
# print("Total Elements:" , b.size)   ## size = total_elements = n(rows)*n(columns) 
# print("Total Dimension:" , b.ndim) ##ndim stands for n_dimensional . 




