def get_square(num):
    return num ** 2

print(get_square(5))

get_square2 = lambda num: num ** 2

print(get_square2(5))

print((lambda num: num ** 2)(10))

l = [1, 2, 3] #2,4,6

def get_double(l):
    return [i * 2 for i in l]

print(get_double(l))

def get_double2(l):
    return list(map(lambda num: num * 2, l))

print(get_double2(l))