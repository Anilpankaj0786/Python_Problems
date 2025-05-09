num=6
for i in range(num,0,-1):
    for j in range(1,i+1):
        if(i==num or j==1 or i==j):
            print("*",end="")
        else:
            print("-",end="")
    print("")
