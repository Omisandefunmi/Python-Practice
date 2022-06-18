characters = "Hello world"
print(characters[10])
print(characters[0: 6] + characters[6:])

my_str = "madam I'm adam"
print(my_str[::-1])
b = "hello world"
print(b[::-2])
c = "hi mom"
d = c[:]
print(d)
f = "yoyo mom"
e = f[::-1]
print(e)

#PalindromeTest

n = 1221
n = str(n)
print(n == n[::-1])

#length
s = 'spam'
print(len(s))
u = 'spam' + '-'+'spam'
print(u*3)

#PrintTriangle

for i in range(11, 0, -1):
    print('* ' * i)
for i in range(1, 11):
    print('* ' * i)

#Type
c = "mexico"
print(type(c))

#manipulatingStrings
a = 'spam'
new_a = a[:1] + 'l' + a[2:]
print(a)
print(new_a)


