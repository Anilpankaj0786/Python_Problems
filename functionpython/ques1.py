# Functions in Python
# Function is reusable block of code .


# Types of Functions
# (a). Pre-defined function  ----> print() , sum() , main() , max() , append() .....
# (b). Manually Created function --->
# step-1 def
# step-2 Name of function
# step-3 logic for create the function
# step-4 Call the function (Name of function)



# # syntax :
# def Name_of_function():
#   logic
# Name_of_function()


# Q.1 Create a function who add 2 numbers ?
def my_add():
    a=4
    b=3
    c=a+b
    print(c)
my_add()


# Q.2 Create a function who add sum of square of a given number ?
def my_squ():
    i=1
    n=3
    sum=0
    while(i<=n):
        sum=sum+i**2
        i=i+1
    print(sum)
my_squ()


# Q.2 Create a function in which user will give a number and we have to calculate sum of this number .
def my_add():
    i=int(input("enter a number"))
    sum=0
    while(i>0):
        r=i%10
        sum=sum+r
        i=i//10
    print(sum)
my_add()




# Arguments and Parameters
# Parameters ---> These are the values which we passes when we create a function .
# Arguments ----> These are the values which we passes when we call a function .

def my_add(a,b):
  c = a + b
  print("Total = ",c)
my_add(3,4)

### here (a,b) ---> Parameters , (3,4) ---> Arguments



# Q.2 Write a program who can check given number is odd or even ?
def oddeven(a):
    if(a%2==0):
        print("even number")
    else:
        print("odd number")
p=int(input("enter a number"))
oddeven(p)

### here (a) ---> Parameter , (49 , p) ----> Argument