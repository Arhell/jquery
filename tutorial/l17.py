words = ['test', 'madam', 'word']
palindromes = []

for word in words:
    if word == word[::-1]:
        palindromes.append(word) # v1

print(palindromes)

palindromes2 = [word for word in words if word == word[::-1]] # v2

print(palindromes2)


my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
palindromes3 = []
for word in my_str:
    word_r = word.replace(' ', '').lower()
    if word_r == word_r[::-1]:
        palindromes3.append(word)

print(palindromes3)

l = list(range(1, 10))
l2 = list('hello')
print(l)

s = '-'.join(map(str, l))
s2 = ','.join(l2)
print(s)
print(s2)