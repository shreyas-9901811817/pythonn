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

first=arr[0]
second=0

for i in range(n):
    for j in range(1,n):
        if (first<arr[j]):
            second=first
            first=arr[j]

print("Second Largest element is : ",second)
