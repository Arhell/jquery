from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('400x300+1000+300')

s = ttk.Style()
# print(s.theme_names())
# s.theme_use('clam')
s.configure('.', foreground="red")

Button(root, text="Button 1", padx=40, pady=5).pack(pady=10)
ttk.Button(root, text="Button 2", width=21).pack()

Entry(root).pack(pady=10)
ttk.Entry(root).pack()


root.mainloop()