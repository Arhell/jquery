list1 = [1, 2, 3]
list12 = [i * 2 for i in list1]
print(list12)

list3 = [1, 2, 3]
res = 0
for num in list3:
  res += num ** 2
print(res)

time1 = 3
time2 = 6.7
time3 = 11.8
print(int(time1 // 2))
print(int(time2 // 2))
print(int(time3 // 2))

print(int(time1 / 2))
print(int(time2 / 2))
print(int(time3 / 2))

s = 'Hello world'
if ' ' in s:
  s = s.upper()
else:
  s = s.lower()
print(s)

