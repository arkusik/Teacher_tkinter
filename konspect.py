import tkinter as tk
from g4f.client import Client
import tk_async_execute as tae
from tkinter import scrolledtext

otvet = ""

async def send_ii(content):
    client = Client()
    response = client.chat.completions.create(
        model = "gpt-4.1",
        messages = [{"role": "user", "content":content}],
        web_search = False
    )
    otvet = response.choices[0].message.content
    _text_area.insert(tk.INSERT, otvet)
    _text_area.configure(state='disabled')

    

def send():
    tae.async_execute(send_ii(entry.get()),wait=True, visible=True, pop_up=True, callback=None, master=root_)




def go_konsp():
    global entry, root_, _text_area

    root_ = tk.Tk()
    root_.attributes("-fullscreen", False)
    root_.geometry("1200x800")

    entry = tk.Entry(root_)
    entry.pack()
    
    but = tk.Button(root_,text="Click", command=send, width=2,height=2)
    _text_area = scrolledtext.ScrolledText(root_, wrap=tk.WORD, width=40, height=20,font=("Arial", 10))
    _text_area.place(x = 500, y = 200)
    clear = tk.Button(root_,text="Clear", command=lambda: _text_area.delete("1.0", tk.END), width=2,height=2)
    but.place(x = 500, y = 40)
    clear.place(x = 700, y = 40)
   
    tae.start()
    root_.mainloop()
    tae.stop()

