from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os
from datetime import datetime



def choose_dir():
  dir_path = filedialog.askdirectory()
  e_path.delete(0, END)
  e_path.insert(0, dir_path)

def f_start():
  dir_path = e_path.get()
  if dir_path:
    for folder, subFolder, file in os.walk(dir_path):
      for file in file:
        path = os.path.join(folder, file)
        mt = os.path.getmtime(path)
        date = datetime.fromtimestamp(mt)
        date = date.strftime('%Y-%m-%d')
        date_folder = os.path.join(path, date)
        if not os.path.exists(date_folder):
          os.mkdir(date_folder)
        os.rename(path, os.path.join(date_folder, file))
    messagebox.showinfo('text', 'text-text')
    e_path.delete(0, END)
  else:
    messagebox.showinfo('text2', 'text-text2')


style = ttk.Style()
s.configure('text3', font=('Helvetiva', 15))

root = Tk()
root.title('Title')
root.geometry('500x150+1000+300')

frame = Frame(root, bg='#56adff', bd=5)
frame.pack(pady=10, padx=10, fill=x)

e_path = ttk.Entry(frame)
e_path.pack(side=LEFT, ipady=2, expand=True, fill=X)

btn_dialog = ttk.Button(frame, text='Text', command=choose_dir)
btn_dialog.pack(side=LEFT, padx=5)

btn_start = ttk.Button(root, text='Text2', style='text3' , command=f_start)
btn_start.pack(fill=x, padx=10)





root.mainloop()