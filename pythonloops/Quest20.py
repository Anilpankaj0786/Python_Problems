for n in range(2,8):
    count=0
    for i in range(2,11):
        if(n%2==0):
            count=1
            break
    if(count==0):
        print("it is prime ", n)
    else:
        print("not a prime ", n)

