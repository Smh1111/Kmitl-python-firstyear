
from tkinter import *
from tkinter import messagebox

Expression = ""
class mobile_phone:
    def __init__(self, window):
        self.number = StringVar()
        
        window.title("KMITL Phone")

        
        self.text = Entry(window, textvariable = self.number, justify="right")
        self.text.grid(row = 1, columnspan=4, ipadx=80, sticky= "W")

        self.button1 = Button(window, width = 12, text = "1", command=lambda:self.ph_no("1"))
        self.button1.grid(row=2, column= 0)

        self.button2 = Button(window, width = 12, text = "2",  command=lambda:self.ph_no("2"))
        self.button2.grid(row=2, column= 1)

        self.button3 = Button(window, width = 12,text = "3", command=lambda:self.ph_no("3"))
        self.button3.grid(row=2, column= 2, sticky= "W")

        self.button4 = Button(window, width = 12,text = "4", command=lambda:self.ph_no("4"))
        self.button4.grid(row=3,  column= 0)

        self.button5 = Button(window, width = 12,text = "5", command=lambda:self.ph_no("5"))
        self.button5.grid(row=3, column= 1,)

        self.button6 = Button(window, width = 12,text = "6", command=lambda:self.ph_no("6"))
        self.button6.grid(row=3, column= 2,sticky= "W")

        self.button7 = Button(window, width = 12,text = "7", command=lambda:self.ph_no("7"))
        self.button7.grid(row=4, column= 0, )

        self.button8 = Button(window, width = 12,text = "8", command=lambda:self.ph_no("8"))
        self.button8.grid(row=4, column= 1, )

        self.button9 = Button(window, width = 12,text = "9", command=lambda:self.ph_no("9"))
        self.button9.grid(row=4, column=2, sticky= "W")

        self.button10 = Button(window, width = 12,text = "*", command=lambda:self.ph_no("*"))
        self.button10.grid(row=5, column= 0, )

        self.button0 = Button(window, width = 12,text = "0", command=lambda:self.ph_no("0"))
        self.button0.grid(row=5, column= 1, )

        self.button11 = Button(window, width = 12,text = "#", command=lambda:self.ph_no("#"))
        self.button11.grid(row=5, column=2, sticky= "E")

        self.talkbutton = Button(window, width = 20, text = "Talk", command=self.Talk)
        self.talkbutton.grid(row=6 , column= 0, columnspan = 2, sticky= "W")

        self.deletebutton = Button(window, width = 20, text = "<", command=self.delete)
        self.deletebutton.grid(row=6 ,column= 1, columnspan = 2, sticky= "E")

    def ph_no(self, ph_no):
        global Expression  
        Expression = Expression + str(ph_no)
        self.number.set(Expression)

    def Talk (self):

        messagebox.showinfo("Dial", f"Dialing <<{self.text.get()}>>")

    def delete(self):
        global Expression
        Expression = Expression[0: len(Expression) - 1]
        
        self.number.set(Expression)


def main():
    window = Tk()
    m = mobile_phone(window)

    window.mainloop()

main()