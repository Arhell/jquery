s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
s2 = set('hello')
s3 = {i for i in range(1, 11)}
s4 = set()

print(s)
print(s2)
print(s3)
print(s4)

nums = [1, 2, 3, 3, 1, 2, 4, 5]
nums2 = set(nums) #list(set(nums))
print(nums2)

a = set('abracadabra')
b = set('alacazam')
c = a - b  # subtraction - we remove from a all the letters that are in b
d = a | b # union the letters without duplicate
e = a & b # intersection - letters that are in a and in b
f = a ^ b # letters a or b, but not both

print(a, b, c, d, e, f, sep='\n')