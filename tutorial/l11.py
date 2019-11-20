l = [1, 2, 3, 'hello', ['test', 10], 'world', True]

l2 = list('hello')
l3 = list((1, 2, 3))

l4 = [i for i in 'hello']
# l5 = [i for i in 'hello world' if i != ' ' and i != ['a']]
l5 = [i for i in 'hello world' if i != ' ' and i not in ['a', 'e', 'i', 'o', 'u', ' ']]

print(l, l2, l3, l4, l5, sep='\n')