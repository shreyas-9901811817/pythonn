def prime(n):
    flag=1
    for i in range(2, n):
        if n % i == 0:
            flag = 0
            break
        else:
            flag = 1
    if flag == 1:
        return 1
    else:
        return 0

n=int(input("Enter a number :"))
large=0
for i in range(2,n+1):
    if n%i==0:
        flag=prime(i)
        if flag==1:
            large=i
print("The largest prime factor is :",large)