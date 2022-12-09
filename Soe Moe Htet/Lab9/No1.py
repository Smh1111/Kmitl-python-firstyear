from tkinter import *

class counter:
    def __init__(self, window):
        self.mainwindow = window
        self.count = 0

        self.text = Label(window, text= self.count)
        self.text.grid(row = 1, column=1)

        self.add_button = Button(window, text = "+", command=self.add)
        self.add_button.grid(row = 2, column=1)

        self.subtract_button = Button(window, text = "-", command=self.subtract)
        self.subtract_button.grid(row = 3, column=1)

        self.reset_button = Button(window, text = "reset", command=self.reset)
        self.reset_button.grid(row = 4, column=1)

    def add(self):
        self.count += 1
        self.text.config(text = self.count)

    def subtract(self):
        self.count -= 1
        self.text.config(text = self.count)

    def reset(self):
        self.count = 0
        self.text.config(text = self.count)

class main():
    window = Tk()
    counter = counter(window)
    window.mainloop()

main()