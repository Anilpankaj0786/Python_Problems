num=5
for i in range(2,num+1):
    for j in range(1,i):
        print(" ",end="")
    for j in range(i,num+1):
        print("*",end=" ")
    print(" ")
    



for i in range(1,num+1):
    x=1
    for j in range(1,i):
        print(" ",end="")
    for j in range(i,num+1):
        print(x,end=" ")
        x+=1
    print(" ")





for i in range(1,num+1):
    x=65
    for j in range(i,num):
        print(" ",end="")
    for j in range(1,i+1):
        print(chr(x),end=" ")
        x+=1
    print(" ")
    




for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print("")
for i in range (4,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print("")
    




for i in range(1,5):
    for j in range(1,i):
        print(" ",end="")

    for j in range(i,5): 
        print("*",end="")
    print("")
for i in range(2,5):
    for j in range(1,5-i):
        print(" ",end="")

    for j in range(1,i+1):
        print("*",end="")
    print("")