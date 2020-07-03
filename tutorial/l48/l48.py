from tkinter import *

root = Tk()

root.geometry('600x400+100+100')

l = Label(root, text="text more text 1\nstring 2\nstring 3\nstring 4\nstring 5\nstring", bg="red",
 fg="#fff", font=("Comic Sans MS", 10, "bold"), justify=CENTER, width=50, height=10, anchor=SW)
l.pack()

img = PhotoImage(file='python.png')
l_logo = Label(root, image=img)
l_logo.pack()

root.mainloop()