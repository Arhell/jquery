t1 = (1, 2, 3)
t2 = 1, 2, 3
t3 = tuple((1, 2, 3))
t4 = ()
t5 = (1,)
t5 = tuple('text')
print(type(t1))
print(t1.__sizeof__())


t6 = tuple('some')
t7 = tuple(' text')
t8 = t6 + t7
print(t8.count('l'))

if 'l' in t8:
  print(t8.index('l'))
else:
  print('text')

for i in t8:
  if i == ' ':
    continue
  print(f'"{i}"', end=' ')


t9 = (10, 11, [1, 2, 3], [4, 5, 6], ['some', 'text'])
print(t9, id(t9))
t9[4][0] = 'new'
t9[4].append('lorem')
print(t9, id(t9))


t10 = (1, 2, 3)
x = t10[0]
y = t10[1]
z = t10[2]
x, y, z = t10

print(x, y, z)

a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)


