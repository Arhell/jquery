d = {}
product1 = {
  'title': 'Sony',
  'price': 100
}

product2 = dict(
  title = 'IPhone',
  price = 110
)

users = {
  ['bob@email.com', 'Bob'],
  ['katy@email.com', 'Katy'],
  ['john@email.com', 'John']
}
d_users = dict(users)

users_t = (
  ('bob@email.com', 'Bob'),
  ('katy@email.com', 'Katy'),
  ('john@email.com', 'John')
)
t_users = dict(users_t)

print(d)
print(product1)
print(product2)
print(users)
print(d_users)
print(t_users)

product3 = dict.fromkeys(['price', 'price2', 'price3'], 50)
print(product3)

nums = {i: i + 1 for i in range(1, 9)}
print(nums)

product4 = {
  'title': 'Sony',
  'price': 100
}

product5 = dict(
  title = 'IPhone',
  price = 110
)

print(product4['title'])
print(product5['price'])
print(product4.get('title'), '') # if no key

# print(nums['1']) # error
print(nums[1])

product6 = dict(
  title = 'IPhone',
  price = 110
)

for key in product6:
  print(f'{key}: {product6[key]}')

for key, value in product6.items():
  print(key, value)

products = [
  {
    'title': 'Sony',
    'price': 100
  },
  {
    'title': 'iphone',
    'price': 110
  },
  {
    'title': 'samsung',
    'price': 90
  }
]

print(products)

for product in products:
  print(product['title'], product['price'])



