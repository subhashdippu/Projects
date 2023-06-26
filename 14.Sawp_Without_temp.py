a = 30
b = 50
c = 3
d = 5
a, b, c, d = b, a, d, c
 
print('a =', a)
print('b =', b)
print('c =', c)
print('d =', d)

# method 2

a = 30
b = 50
 
a = a + b # a=80, b=50
b = a - b # a=80, b=30
a = a - b # a=50, b=30
 
print('a =', a)
print('b =', b)