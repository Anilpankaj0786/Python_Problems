import numpy as np 

# Operations on Array `


a = np.arange(1,16,1)
a

a>10 


b = a>10 
a[b]

a[a%2==0] 

a[a%2!=0]

a = np.arange(1,5)
a




# Reshaping the Array

# n(rows)*n(columns) = total_elements


a = np.arange(1,13)
a

a.shape


# 1*12 , 12*1 
# 2*6 , 6*2 
# 3*4 , 4*3 


a.reshape(2,6)


a.reshape(3,4)


a.reshape(4,3)


a.reshape(5,3)



a = np.arange(1,5).reshape(2,2)
a


b = np.arange(5,9).reshape(2,2)
b


a+b  ### (1+5 = 6 , 2+6 = 8 , 3+7=10 , 4+8 = 12)    

a-b  ### (1- 5 = -4 , 2-6 = -4 , 3-7 = -4 , 4-8 = -4)

a*b  ### (1*5 = 5 , 2*6 = 12 , 3*7 = 21 , 4*8 = 32)

a.dot(b)    ## for matrix multiplication 

a/b

a**2

a**3

# LinSpace() ----> It will return same gap values in a given range . 

a = np.linspace(1,2,5)
a
# output: 1.0 , 1.25 , 1.5 , 1.75 , 2.0
# 1.25-1 = 0.25 
# 1.5-1.25 = 0.25
# 1.75-.1.50 = 0.25 
# 2-1.75 = 0.25


# unique() ----> It will provide an array in which it will return 3 array . 
# arr ---> return unique values 
# return_index = True ----> return indexing of unique values . 
# return_counts = True ----> return frequrncy of each unique value


a = np.array([1,2,3,1,1,1,2,6,7])
a

np.unique(a , return_index=True , return_counts=True) 

a = np.arange(1,10).reshape(3,3)
a

np.sum(a) 

np.sum(a , axis = 0)   ### returns column wise sum 

np.sum(a , axis = 1)   ### return row wise sum 


# hstack and vstack

a = np.arange(1,5)
b = np.arange(5,9)
c = np.arange(9,13)

np.hstack((a,b,c))

np.vstack((a,b,c))

a = np.arange(1,5)
a

np.sqrt(a) 

np.sin(a) 

np.cos(a) 
