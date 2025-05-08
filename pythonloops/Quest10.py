
n=12363
reverse=0
while(0<n):
    remainder=n%10
    reverse=reverse*10+remainder
    n=n//10
print(reverse)
