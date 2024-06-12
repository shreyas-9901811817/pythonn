a=10
b=20
print(a>b)
print(b>a)
print(bool("qwerty"))

print( a is b)
print(a is not b)


list= ['apple','banana','cherry',123]
list.append('mango')
print(list)
list.pop(4)
print(list)
print(type(list))
list[1]='watermelon'
print(list)
list.insert(1,'chickoo')
print(list)
print('apple' in list) #Membership operator
print(list.index('cherry'))
print(len(list))
print(list[0:2])
print(list[-2])

b=['car','bus']
print(list+b)
list.extend(b) #pop,remove(name)
print(list)

a=['aaa','ccc','bbb']
b=[-11,34,12]
a.sort()
b.sort(reverse=True)
print(a)
print(b)

a.reverse()
print(a)

c=a.copy()
print(c)
print('\n\n')
for l in list:
    print(l)