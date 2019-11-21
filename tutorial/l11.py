l = [1, 2, 3, 'hello', ['test', 10], 'world', True]

l2 = list('hello')
l3 = list((1, 2, 3))

l4 = [i for i in 'hello']
# l5 = [i for i in 'hello world' if i != ' ' and i != ['a']]
l5 = [i*2 for i in 'hello world' if i != ' ' and i not in ['a', 'e', 'i', 'o', 'u', ' ']]

print(l, l2, l3, l4, l5, sep='\n')

l6 = list(range(0, 11, 2))

print(l6)

for i in range(1, 3):
  print(f'Out #{i}')
  for j in range(1, 3):
    print(f'In #{j}')