for i in range(5):
    for j in range(5):
        print('*',end='  ')
    print()


print('\n\n')

a=0

for i in range(5):
    b = 5
    b=b-i
    for j in range(a):
        print('',end=' ')
    for k in range(b):
        print(f'{b}',end=' ')
        b=b-1
    a=a+1
    print()


for i in range(5):
    for j in range(i):
        print(" ", end="")

    for k in range(5 - i, 0, -1):
        print(k, end=" ")

    print()


print('\n\n')








for i in range(5):
    for j in range(5):
        if (i==j) or (i+j==4):
            print('* ',end='')
        else:
            print('',end='  ')
    print()













print()
print()



a="abcd"