from tkinter import *
import time

root = Tk()
root.title('Counter')

root.geometry('600x400+100+100')

def ckeck_time():
  btn_time['text'] = time.strftime('%H:%M:%S')

clicks = 0

def counter():
  global clicks
  clicks += 1
  root.title(f'Counter: {clicks}')

btn_time = Button(root, text="check time", command=ckeck_time)
btn_time.pack()

btn_cnt = Button(root, text="Counter", command=counter)
btn_cnt.pack()

root.mainloop()