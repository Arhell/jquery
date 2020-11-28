# from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
root = Tk()

root = ThemedTk(theme="acr")
root.geometry("400x300+1000+300")

ttk.Button(root, text="Button").pack(pady=10)
ttk.Entry(root).pack()


root.mainloop()