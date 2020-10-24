from tkinter import *
from tkinter import ttk
import urllib.request
import json
from tkinter import messagebox

root = Tk()
root.title('Title')
root.geometry('300x250+1000+300')
root.resizable(False, False)

START_AMOUNT = 1000

def exchange():
  pass

header_frame = Frame(root)
header_frame.pack(fill=X)
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

h_currency = Label(header_frame, text="Text", bg="#ccc", font="Arial 12 bold")
h_currency.grid(row=0, column=0, stiky=EW)
h_buy = Label(header_frame, text="Text", bg="#ccc", font="Arial 12 bold")
h_buy.grid(row=0, column=1, stiky=EW)
h_sale = Label(header_frame, text="Text", bg="#ccc", font="Arial 12 bold")
h_sale.grid(row=0, column=2, stiky=EW)

usd_currency = Label(header_frame, text="USD", font="Arial 10")
usd_currency.grid(row=1, column=0, stiky=EW)
usd_buy = Label(header_frame, text=JSON_object[0]['buy'], font="Arial 10")
usd_buy.grid(row=1, column=1, stiky=EW)
usd_sale = Label(header_frame, text=JSON_object[0]['sale'], font="Arial 10")
usd_sale.grid(row=1, column=2, stiky=EW)

eur_currency = Label(header_frame, text="USD", font="Arial 10")
eur_currency.grid(row=1, column=0, stiky=EW)
eur_buy = Label(header_frame, text=JSON_object[1]['buy'], font="Arial 10")
eur_buy.grid(row=1, column=1, stiky=EW)
eur_sale = Label(header_frame, text=JSON_object[1]['sale'], font="Arial 10")
eur_sale.grid(row=1, column=2, stiky=EW)

rur_currency = Label(header_frame, text="USD", font="Arial 10")
rur_currency.grid(row=1, column=0, stiky=EW)
rur_buy = Label(header_frame, text=JSON_object[2]['buy'], font="Arial 10")
rur_buy.grid(row=1, column=1, stiky=EW)
rur_sale = Label(header_frame, text=JSON_object[2]['sale'], font="Arial 10")
rur_sale.grid(row=1, column=2, stiky=EW)

calc_frame = Frame(root, bg="#fff")
calc_frame.pack(extand=1, fill=BOTH)
calc_frame.grid_columnconfigure(1, weight=1)

l_uah = Label(calc_frame, text="Text", bg="#fff", font="Arial 10 bold")
l_uah.grid(row=0, column=0, padx=10)
e_uah = ttk.Entry(calc_frame, justify=CENTER, font="Arial 10")
e_uah.grid(row=0, column=1, columnspan=2, pady=10, padx=10, stiky=EW)
e_uah.insert(0, START_AMOUNT)

btn_calc = ttk.Button(calc_frame, text="text", command=exchange)
btn_calc.grid(row=1, column=1, columnspan=2, stiky=EW, padx=10)

res_frame = Frame(root)
res_frame.pack(extand=1, fill=BOTH, pady=5)
res_frame.grid_columnconfigure(1, weight=1)

l_usd = Label(res_frame, text="text", font="Arial 10 bold")
l_usd.grid(row=2, column=0)
e_usd = ttk.Entry(res_frame, justify=CENTER, font="Arial 10")
e_usd.grid(row=2, column=1, columnspan=2, padx=10, stiky=EW)
e_usd.insert(0, round(START_AMOUNT / float(JSON_object[0]['sale']), 2))


l_eur = Label(res_frame, text="text", font="Arial 10 bold")
l_eur.grid(row=3, column=0)
e_eur = ttk.Entry(res_frame, justify=CENTER, font="Arial 10")
e_eur.grid(row=3, column=1, columnspan=2, padx=10, stiky=EW)
e_eur.insert(0, round(START_AMOUNT / float(JSON_object[0]['sale']), 2))

l_rur = Label(res_frame, text="text", font="Arial 10 bold")
l_rur.grid(row=4, column=0)
e_rur = ttk.Entry(res_frame, justify=CENTER, font="Arial 10")
e_rur.grid(row=4, column=1, columnspan=2, padx=10, stiky=EW)
e_rur.insert(0, round(START_AMOUNT / float(JSON_object[0]['sale']), 2))







root.mainloop()