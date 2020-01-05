# import os
# print(os.getcwd())
#
#
# import random as r
# print(r.randint(1, 100))
#
#
# import random
# print(random.randint(1, 100))
#
#
# from random import randint, shuffle
# print(randint(1, 50))
#
# l = [1, 2, 3, 4, 5]
# shuffle(l)
# print(l)


# from random import *

import lib

# print(lib.get_count('hello', 'l'))
# print(lib.get_len('hello'))

f = lib.get_count
print(f('hello', 'l'))

def get_sum(a, b):
  return  a + b

func = get_sum

print(func(1, 2))