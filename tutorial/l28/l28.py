import os

def read_dir(f):
  for root, dirs, files in os.walk(f):
    level = root.count(os.sep)
    indent = ' ' * 4 * level
    print(f'{indent}[{os.path.basename(root)}]')
    sub_indent = ' ' * 4 * (level + 1)
    for file in files:
      print(f'{sub_indent}{file}')



read_dir('folder')
