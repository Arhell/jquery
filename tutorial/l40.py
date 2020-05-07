import re

s = "some text some text. some text some text."
patter = "some"

if re.search(patter, s):
  print("some text")
else:
  print("Some")

match = re.search(patter, s)
print(match)
print(match.start())
print(match.end())

print(re.match(patter, s))

print(re.findall(patter, s))

print(re.split(r'\.', s, 1))

a = '''some text.
Some text some text
some text: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10
Some text: "!", "@", "-", "&", "?", "_"
a\\b\tc
test string
'''

pat = r'\w+'
pat2 = r'[a-z0-9]+'
pat3 = r'[\da-]+'
pat4 = r''
pat5 = r'\w+$'


print(re.findall(pat, a))
print(re.findall(pat2, a, flags=re.IGNORECASE))
print(re.findall(pat3, a, flags=re.IGNORECASE))
print(re.findall(pat4, a, flags=re.IGNORECASE))
print(re.findall(pat5, a, flags=re.IGNORECASE))

def val_email(email):
  return re.match(r"^.+@(\w+\.){0,2}[a-z]{2,6}$", email, re.IGNORECASE)

print(val_email('mail@mail.com'))



