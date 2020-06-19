from tkinter import *

root = Tk()

root.geometry('600x400+100+100')

def clicked():
  print('Clicked')

# btn = Button(root, text='button', command=clicked, font=("Comic Sans MS", 20))
btn = Button(root, text='button\n22', justify=LEFT)
btn.configure(width=20, heigth=5)
btn['font'] = 'Arial'
btn.pack()




root.mainloop()