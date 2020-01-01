def get_sum(a, b):
  """
  :return sum args a anb b

  :param a: first operand
  :type a: int
  :param b: second operand
  :type b: int
  :return: return type int
  """
  return a + b

print(get_sum(1, 2))

a = 5 # global
def f():
  a = 10 # local
  a += 1
  print(a)

print(a)
f()
print(a)

def f2():
  global a
  a += 1

print(a)
f2()
print(a)

l = [1, '2', 3]

def d(l):
  return [i * 2 for i in l]

print(d(l))

def d2(l):
  def get_mult(x):
    return int(x) * 2
  return [get_mult(i) for i in l]

print(d2(l))

def d3(l):
  def get_mult(x):
    if isinstance(x, int):
      return x * 2

  return [get_mult(i) for i in l if get_mult(i)]

print(d3(l))

def d4(l):
  def get_mult(x):
    return x * 2

  return list(map(get_mult, l))

print(d4(l))