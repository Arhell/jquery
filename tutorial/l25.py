def odd_ball(arr):
  return arr.index('odd') in arr

print(odd_ball(['even', 4, 'even', 7, 'even', 55, 'even', 6, 'even', 10, 'odd', 3, 'even']))
print(odd_ball(['even', 4, 'even', 7, 'even', 55, 'even', 6, 'even', 9, 'odd', 3, 'even']))
print(odd_ball(['even', 10, 'odd', 2, 'even']))

def find_sum(n):
  res = 0
  for i in range(n + 1):
    if i % 3 == 0 or i % 5 == 0:
      res+=1
  return res

print(find_sum(5))
print(find_sum(10))

def find_sum2(n):
  return sum(i for i in range(n+1) if i % 3 == 0 or i % 5 == 0)

print(find_sum2(5))
print(find_sum2(10))


names = ['Ryan', 'Kieran', 'Mark', 'John', 'David', 'Paul']
def get_names(names):
  return [i for i in names if len(i) == 4]

print(get_names(names))



