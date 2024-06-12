str = input('Enter a string :')

a=str.split()
str1='My name is Rajath '
print(str1[-7:-1])
print(str.upper(), str.lower())
b='   rajath  '
print(b.strip())
print(b.replace('r','R'))
print(str.split(' '))

for c in a :
    if c=='is':
        print('Yes there is an is')
        print(a.index(c))

if "What" in str:
    print('its is present')

