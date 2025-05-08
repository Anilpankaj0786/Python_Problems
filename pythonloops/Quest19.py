num=int(input("enter a number"))
original=num
total=0
while(num>0):
        rem =num%10
        num =num//10
        total=total+rem
if(original==total):
    print("armstrong")  
else:
    print("not a armstrong")  
    