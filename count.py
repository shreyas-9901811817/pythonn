n=int(input("Enter the size of an Array : "))

if n>=1 and n<=1051:
    x = int(input("Enter the value of X : "))
    if x>=1 and x<=106:
        print("Enter the array items : ")
        count = 0
        for i in range(n):
            a = int(input())
            if a >= 1 and a <= 1061:
                if a == x:
                    count = count + 1

    print(f'The number of occurance of {x} in Array is : {count}')
