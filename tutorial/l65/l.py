from tkinter import ttk
from ttkthemes import ThemedTk
import request
from tkinter import messagebox

API_KEY = ''
API_URL = ''

def get_weather():
    if not entry.get():
        messagebox.showwarning('warning', 'Add')
    else:
        params = {
            "appid": API_KEY,
            "q": entry.get(),
            "units": "metric",
            "lang": "en"
        }
        r = request.get(API_URL, params=params)
        weather = r.json()
        

root = ThemedTk(theme="arc")
root.geometry("500x400+1000+300")
root.resizable(0, 0)

top_frame = ttk.Frame(root)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.5, relheigth=0.1, anchor='n')

entry = ttk.Entry(top_frame)
entry.place(relwidth=0.7, relheigth=1)

button = ttk.Button(top_frame, text="Text", command=get_weather)
button.place(relx=0.7, relwidth=0.3, relheigth=1)

lower_frame = ttk.Frame(root)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheigth=0.6, anchor='n')

label = ttk.Label(lower_frame, anchor="nw")
label.place(relwidth=1, relheigth=1)

root.mainloop()

