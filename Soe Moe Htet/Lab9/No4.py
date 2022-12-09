from tkinter import *
from random import randint
import tkinter.messagebox

class paint:
    def __init__(self, window):
        self.window = window
        self.window.title("Tk")

        self.colors = ["red", "blue", "orange", "yellow", "cyan"]
        
     
        self.canvas = Canvas(
            window, 
            width = 500, 
            height = 200, 
            bg = "white"
            )

        
        self.canvas.bind("<Button- 1>", self.draw)
        
        self.canvas.create_rectangle(30, 30, 450, 150, tags = "rect")
        self.clear = Button(self.window, text = "Clear", command=self.clear)
        self.clear.pack()
        
        self.canvas.pack()
        self.window.mainloop()


    def draw(self, event):
        
        self.x1 = event.x - 5
        self.y1 = event.y - 5
        self.x2 = event.x + 5
        self.y2 = event.y + 5

        if (event.x < 30 or event.x > 450 and event.y < 30 or event.y > 150 ):
            tkinter.messagebox.showinfo("Warning", "Mouse pointer is not in the rectangle")

        else:


            index = randint(0, len(self.colors)-1)

            self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill = f"{self.colors[index]}")

        


    def clear(self):

        self.canvas.delete("all")
        self.canvas.create_rectangle(30, 30, 450, 150, tags = "rect")

def main():
    window = Tk()
    p = paint(window)


main()