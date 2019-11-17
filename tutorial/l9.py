x = 1
if x:
  print('x = True')
else:
  print('x = False')

light = 'red'
if light == 'red':
  print('Stop')
elif light == 'yellow':
  print('Wait')
elif light == 'green':
  print('Go')
else:
  print('Text')

age = int(input('Some text num'))

if age >= 18:
  print('1')
else:
  print(f'{age} 2')

time = 12
day = 'st'
if time < 12 or time > 13:
    print('Open')
else:
    print('Close')

if time >= 8 and day != 'su':
  print('Open')
else:
  print('Close')

b = 1
if not b:
  print('ok')
else:
  print('no')

a = 1
res = 'ok' if a else 'no'
print(res)