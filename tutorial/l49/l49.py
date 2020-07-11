from tkinter import *

root = Tk()

root.geometry('600x400+100+100')

def add_str():
    e.insert(END, 'text')

def del_str():
    e.delete(0, END)

def get_str():
    l_text['text'] = e.get()

l = Label(root, text="Text")
l.pack()

e = Entry(root)
# e.insert(0, 'text')
# e.insert(END, ' text2')
e.pack()

btn_add = Button(root, text="Add", command=add_str).pack()
btn_del = Button(root, text="Delete", command=del_str).pack()
btn_get = Button(root, text="Get", command=get_str).pack()

l_text = Label(root, bg='red', fg='white')
l_text.pack(fill=X)

root.mainloop()