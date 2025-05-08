lcm of two number
a=32
b=108
max_val=max(a,b)
while(True):
    if(max_val%a==0 and max_val%b==0):
        break 
    max_val+=1
print(max_val)
