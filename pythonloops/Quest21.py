# # sum of prime digits
# n = int(input("Enter the digit: "))
# sum_prime = 0

# while n > 0:
#     digit = n % 10  # Extract the last digit
#     if digit in {2, 3, 5, 7}:  # Check if the digit is prime
#         sum_prime += digit
#     n //= 10  # Remove the last digit

# print("Sum of prime digits:", sum_prime)



n= input("enter a number")
original_val=n
i=0
count=0
p=1
while(0<original_val):
    
    original_val=original_val//10
    count+=1
while(count-1>0):
    p=p*10
    count-=1
print(p)
first=n//p
print("first number",first)
if first==0:
    print("this number is not a duck number")
    

