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

l1 = [1, 2, 3]
# l2 = l1
# l2 = l1.copy()
l2 = l1[:]
l1.append((5))
print(l1, id(l2))

r = 10
print(r)
del r
print(r)
