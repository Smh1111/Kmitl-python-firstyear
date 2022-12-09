from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('Python Guides')
ws.geometry('400x300')

def clicked():
    messagebox.showinfo('sample 1', 'this is a message')
    messagebox.showinfo('sample 2', 'this is a message to change the size of box')
    messagebox.showinfo('sample 3', ' this is the message that is larger than previous message.')

Button(ws, text='Click here', padx=10, pady=5, command=clicked).pack(pady=20)

ws.mainloop()