n=int(input("Enter the value of n :"))
arr=[]
print("Enter the values :")
for i in range(n):
    a=int(input())
    arr.append(a)

for x in range(n):
    for y in range(n-1):
        if (arr[y]>arr[y+1]):
            temp=arr[y]
            arr[y]=arr[y+1]
            arr[y+1]=temp
print(arr)
print("Output : ",end=' ')
a=0
for i in range(n):
    for j in range(0,n-1):
        if i!=j:
            if arr[i] == arr[j]:
                a=1
                print(arr[i], end=' ')
                arr[i]= ''
                break
else:
    if a==0:
        print('-1')