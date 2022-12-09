
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo

class currency_exchanger:
    def __init__(self, window):
        self.window = window
        self.money = 0

        window.title("Currecny Converter")
        
        self.input_money = IntVar()
        
        self.input_button = Entry(textvariable = self.input_money, justify="right")
        self.input_button.grid(row = 1, column= 1)

        

        self.usd_to_thb = Button(window, text = "USD -> THB", command=self.usd_to_thb)
        self.usd_to_thb.grid(row = 2, column = 1)

        self.thb_to_usd = Button(window, text = "THB -> USD", command=self.thb_to_usd)
        self.thb_to_usd.grid(row = 3, column = 1)

    def usd_to_thb (self):
        self.money = int(self.input_button.get())
        amount = self.money * 30

        #info = messagebox(self.window, title = "USD -> THB", text = f"{self.money:.2f} USD = {int(amount):.2f} THB") 
        #info.grid(row=4, column = 1)

        messagebox.showinfo("USD -> THB", f"{self.money:.2f} USD = {amount:.2f} THB")
        
    def thb_to_usd(self):
        self.money = int(self.input_button.get())
        amount = self.money / 30
        messagebox.showinfo("THB -> USD", f"{self.money:.2f} THB = {amount:.2f} USD")

def main():

    window = Tk()
    c = currency_exchanger(window)

    window.mainloop()

main()