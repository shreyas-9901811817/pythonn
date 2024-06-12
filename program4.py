n=int(input("Enter the value of n :"))
if n>=1 :
    arr=[]
    print("Enter the values :")
    for i in range(n-1):
        a=int(input())
        arr.append(a)
    print(f'The array is : {arr}')

    for x in range(n-1):
        for y in range(n-2):
            if (arr[y]>arr[y+1]):
                temp=arr[y]
                arr[y]=arr[y+1]
                arr[y+1]=temp

    # print("The Sorted array is :", arr)

    for x in range(1,n):
        flag=0
        for y in range(0,n-1):
            if arr[y]==x:
                flag=1
                break
        if flag==0:
            print(x,end=' ')


    # i = 0
    # for j in range(1, n + 1):
    #     if j != arr[i]:
    #         print(i + 1, end=' ')
    #         i -= 1
    #     i += 1
