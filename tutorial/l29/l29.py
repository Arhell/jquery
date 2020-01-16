f = open('file.txt', 'r', encoding='utf=8')
text = f.read(1)
text2 = f.read()

f.close()
print(text)
print(text2)


f = open('file.txt', 'a', encoding='utf=8')
f.write('new string\n')
f.close()


lines = ['new string 1', 'new string 2']
f = open('file.txt', 'a', encoding='utf=8')
for i in lines:
  f.write(i + '\n')
f.writelines(lines)
f.writelines(f'{i}\n' for i in lines)
f.close()


f = open('file.txt', 'r', encoding='utf=8')
for line in f:
  print(line.replace('\n', ''))
  print(line, end='')
f.close()


lines = ['new string 1', 'new string 2']
f = open('file2.txt', 'w', encoding='utf=8')
f.writelines(f'{i}\n' for i in lines)
f.close()