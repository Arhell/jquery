l = [1, 2, 3, 'hello', ['test', 10], 'world', True]
name = ['some', 'text', 'lorem']

l[2] = 'world'
l[:2] = [10, 15]
print(l[0:3])

l.append('new')
l.extend([5, 7])
l2 = ['hi', 19]
l += l2
l.insert(1, 'elem')
# l.remove('world')
el = l.pop(1)
print(l, el)

l3 = ['hello', 'hi', 'text', 'some']
l3.sort()
l3 = l3.sorted(l3)
print(l3)

print(l, l.count('world'))
