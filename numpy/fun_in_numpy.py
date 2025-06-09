# Functions in Numpy 
# (1). zeros() ----> It will create an array in which all the values in either one dimensional or 
# multi-dimensional will be 0 . 


import numpy as np

a = np.zeros(3) 
a


a = np.zeros((3,4))
a


# (2). ones() ----> It will crreate an array in which all the values will be 1 in either one 
# dimensional or multi-dimensional . 

a = np.ones(3) 
a

a = np.ones((3,4))
a

# (3). eye() -----> 
# Matrix ---> digonal Position ---> 1 
# It will create an array in which digonal positinoal elements will be 1 and rest all are 0 . 
a = np.eye(3)
a


a = np.eye(3,4)
a


# (4). diag() ----> It will create an array in which you can set custom values at digonal position . 

# (5). Random Module ----> It will return random numbers . 
# (a). Randint() ----> It will return random numbers in a given range .
# syntax: 
# np.random.randint(min_number ,max_number , total_numbers) 

a = np.random.randint(1,10,3)
a

# (b). rand() ---> It will provide random numbers in range of 0 to 1 . 
a = np.random.rand(4)
a

# Random Numbers ---> data use ---> Output 
# if random numbers refresh update ---> previous output change . 

# (c). seed() ----> It will fix our random generated data . 
np.random.seed(15) 
a = np.random.randint(1,10,3)
a


# View  vs Copy 
# view means modification in original data and copy means modification in duplicate data . 
a = np.array([10,20,30,40,50,60,70,80,90])
a


b = a[3:6]
b[:] = 0
b


a


a = np.array([10,20,30,40,50,60,70,80,90])
b = a[3:6].copy()
b[:] = 0
b

