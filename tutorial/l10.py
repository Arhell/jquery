i = 1
while i <= 10:
  print(i, end=' ')
  i += 1

s = 'Hello world'
for l in s:
  if l == ' ':
    continue
  print(f'"{l}"', end=' ')

for i in 'Hello world':
  if i == ' ':
    break
  print(i, end=' ')
else:
  print('\nNo spaces')

year = 1900
while year <= 2020:
  print(year)
  year += 1
else:
  print('Done')
