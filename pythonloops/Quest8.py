n= int(input("enter a number"))
i=0
sum=0
while(0<n):
    
    r=n%10
    sum+=r
    n=n//10
print(sum)