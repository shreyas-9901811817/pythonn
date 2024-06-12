n=int(input("Enter the size of an Array :"))

if n>=1 and n<=1051:
    x = int(input("Enter the value of X :"))
    if x <= 106 and x >= 1:
        print("Enter the array items :")
        Arr = []
        count = 0

        for i in range(n):
            a = int(input())
            if a<=1061 and a>=1:
                Arr.append(a)
                if a == x:
                    count = count + 1

        print("The array is : ", Arr)
        print(f'The number of occurance of {x} in Array is : {count}')

    else:
        print("The value of x should be in between 1 and 106")
else:
    print("The value of n should be in between 1 and 1051")