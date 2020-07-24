from tkinter import *

root = Tk()

# def color_red():
#     l['text'] = 'red'
#     e.delete(0, END)
#     e.insert(0, '#ff0000')

# def color_orange():
#     l['text'] = 'orange'
#     e.delete(0, END)
#     e.insert(0, '#ff7d00')
#
# def color_yellow():
#     l['text'] = 'yellow'
#     e.delete(0, END)
#     e.insert(0, '#ffff00')

def get_color(text_color, hex_color):
    l['text'] = text_color
    e.delete(0, END)
    e.insert(0, hex_color)

l = Label(root)
e = Entry(root, width=30, justify='center')
l.pack()
e.pack()

colors = {
    "#ff0000": "red",
    "#ff7d00": "orange",
    "#ffff00": "yellow"
}

for key, value in colors.items():
    Button(root, bg=key, command=lambda text=value, hex=key: get_color(text, hex)).pack(fill=X)


# btn_red = Button(root, bg='#ff0000', command=lambda: get_color('red', '#ff0000')).pack(fill=X)
# btn_orange = Button(root, bg='#ff7d00', command=lambda: get_color('orange', '#ff7d00')).pack(fill=X)
# btn_yellow = Button(root, bg='#ffff00', command=lambda: get_color('yellow', '#ffff00')).pack(fill=X)
# btn_orange = Button(root, bg='#ff7d00', command=color_orange).pack(fill=X)
# btn_yellow = Button(root, bg='#ffff00', command=color_yellow).pack(fill=X)




root.mainloop()