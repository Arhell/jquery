from tkinter import *

root = Tk()
root.geometry("400x300+1000x300")

def f_event(event, key):
  print(event, key)

l = Label(root, bg="blue")
l.pack(fill=X, expand=1)
l.bind("<Button-1>", f_event)

e = Entry(root, justify=CENTER, font="Arial 15")
e.pack(fill=X, expand=1, padx=10, ipady=10)
e.bind("<Button-2>", lambda f_event, key="Middle clock": f_event(event, key))
e.bind("<Button-3>", lambda f_event, key="Right clock": f_event(event, key))
e.bind("<FocusIn>", lambda f_event, key="Focus": f_event(event, key))

l2 = Label(root,bg="#fff")
l2.pack(pady=10, fill=X)

colors = {
  "#ff0000": "1",
  "#ff7d00": "2",
  "#ffff00": "3",
  "#00ff00": "4",
  "#007dff": "5",
  "#0000ff": "6",
  "#7d00ff": "7"
}

class MyLabels:
  def __init__(self, master, color):
    self.color = color
    self.b = Label(master, bg=color, width=4, height=2)
    self.b.pack(side=LEFT, padx=1)
    self.b.bind("Button-1", lambda event, key="1": self.get_color(event, key))
    self.b.bind("Button-3", lambda event, key="1": self.get_color(event, key))

  def get_color(self, event, key):
    if key == "1":
      l2['bg'] = self.color
    else:
      l2['bg'] = "#fff"

for k, v in colors.items():
  MyLabels(root, k)


root.mainloop()