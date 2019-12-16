words = ['test', 'madam', 'word']
palindromes = []

for word in words:
    if word == word[::-1]:
        palindromes.append(word) # v1

print(palindromes)

palindromes2 = [word for word in words if word == word[::-1]] # v2

print(palindromes2)