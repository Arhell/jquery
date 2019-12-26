product1 = { 'title': 'Sony', 'price': 100 }
print(product1.items())
print(product1.keys())
# print(product1.pop('title', 'no'))
print(product1.setdefault('title', 'test'))

product2 = { 'title': 'Sony', 'price': 100 }
product2.update({'test': 'value'})
product2.update({'price': '310'})
print(product2.values())

