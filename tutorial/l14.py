x = 10
print(x, id(x))
x = 20
print(x, id(x))

s = 'some'
print(s, id(s))
s += ' text'
print(s, id(s))

l = [1, 2, 3]
print(l. id(l))
l.append(5)
print(l, id(l))


a = 10
b = a
print(a, id(a))
print(b, id(b))

a = 15
print(a, id(a))
print(b, id(b))