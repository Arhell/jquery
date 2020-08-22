from tkinter import *

root = Tk()
root.geometry('600x400+1000+300')

# l1 = Label(root, text="Hello world", bg="#3498db", fg="#ffff", font="16", padx=20, pady=8)
# l1.place(x=0, y=0, anchor="w")
#
# l1 = Label(root, text="Hello world", bg="#2ecc71", fg="#ffff", font="16", padx=20, pady=8)
# l1.place(relx=0.5, rely=0.5, anchor=CENTER)

# btn1 = Button(text="Button 1", bg="#3498db", fg="#ffff", font="16", padx=20, pady=8)
# btn1.place(x=0, y=0)
#
# btn2 = Button(text="Button 2", bg="#2ecc71", fg="#ffff", font="16", padx=20, pady=8)
# btn2.place(relx=0.5, rely=0.5, anchor="c")
#
# btn3 = Button(text="Button 3", bg="#f1c40f", fg="#ffff", font="16", padx=20, pady=8)
# btn3.place(relx=1, rely=1, anchor="se")

l = Label(root, bg="#000")
l.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

root.mainloop()