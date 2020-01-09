import random
import locale
from datetime import date, datetime, timedelta

x = random.randint(1, 100)
user_num = 0
cnt = 0

while True:
  user_num = int(input('Some text some text'))
  cnt += 1 # cnt = cnt + 1
  if user_num == x:
    print(f'Some text {cnt}')
    if input('Some text' == 'y'):
      x = random.randint(1, 100)
      cnt = 0
    else:
      print('some text')
      break

    print('some text')
    break

  elif user_num > x:
    print('Some text')

  else:
    print('Some text')


from datetime import date, datetime

# date
today = date.today()
print(today)
print(today.day)

# datetime

now = datetime.now()
now2 = datetime.today()

print(now, now2, sep = '\n')

days = ['Mn', 'Ts', 'Wn', 'Tr', 'Fr', 'St', 'Sn']
print(days[now.weekday()])

locale.setlocale(locale.LC_ALL, 'en_Us, UTF-8')

now3 = datetime.now()
print(now3.strftime('%A'))

print(f'Date: {now.strftime("%A, %d %B %Y")}')
print(f'Time: {now.strftime("%H: %M: %S")}')

print(now.strftime('%c'))
print(now.strftime('%x'))
print(now.strftime('%X'))

now4 = datetime.today()

print(now4.strftime('%c'))
d1 = now4 + timedelta(days=1, hours=2, minutes=10)
print(d1.strftime('%c'))