n  = int(input('Enter the value of n :'))

for i in range(2,n+1):
    flag=0
    for j in range(2,i-1):
        if (i % j == 0):
            flag=1
    if flag==0:
        print(f'{i}',end=' ')