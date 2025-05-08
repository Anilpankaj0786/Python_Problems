
n= int(input("enter a number"))
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
first=n//p
print("first number",first)
last=n%10
print("last number",last)
sum=first+last
print(sum)