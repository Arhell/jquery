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




