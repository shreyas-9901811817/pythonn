print("Enter the the value for a and b :")
a=int(input())
b=int(input())
q=0
n=abs(a)
if abs(a)>abs(b):
    for i in range(n):
        if(abs(a)-abs(b)>=0):
            a=abs(a)-abs(b)
            q=q+1

if (a<0 and b<0) or (a>0 and b>0):
    neg=0
else:
    neg=1

if neg==1:
    q=-q

print("Quotient is ",q)

#13 2 6
#14 -2 -7
#-11 2 -5