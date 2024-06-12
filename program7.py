n=int(input("Enter the value of n :"))
arr=[]
print("Enter the values :")
for i in range(n):
    a=int(input())
    arr.append(a)

jump=arr[0]
j=0
count=0
for i in range(n):
    if jump==0:
        count=-1
        break
    if (jump+j<n):
        jump=arr[j+jump]
        j=jump
        count=count+1
    else:
        count=count+1
        break
print("Number of Jumps is :",count)
