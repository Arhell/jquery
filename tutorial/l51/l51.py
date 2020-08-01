from tkinter import *

root = Tk()

colors = {
    "#ff0000": "red",
    "#ff7d00": "orange",
    "#ffff00": "yellow"
}

l = Label(root)
e = Entry(root, width=30, justify='center')
l.pack()
e.pack()

class MyButtons:
    def __init__(self, master, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.button = Button(root, bg=hex_color, command=self.get_color)
        self.button.pack(fill=X)

    def get_color(self):
        l['text'] = self.text_color
        e.delete(0, END)
        e.insert(0, self.hex_color)

for key, value in colors.items():
    MyButtons(root, value, key)

root.mainloop()