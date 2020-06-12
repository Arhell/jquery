from tkinter import *

root = Tk()
root.title('GUI app')
root.iconbitmap()
root.geometry('600x400+100+100')
root.resizable(False, False)
# root.config(bg='red')
root['bg'] = 'red'

root.mainloop()