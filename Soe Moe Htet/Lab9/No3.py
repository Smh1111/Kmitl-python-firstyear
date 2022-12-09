from tkinter import *

class paint:
    def __init__(self, window):
        self.window = window
        self.window.title("A simple paint program")


        # colors = ["red", "blue", "orange"]
        
        
        
        self.canvas = Canvas(window, width = 500, 
        height = 500, bg = "white")

        

        self.canvas.bind("<B1-Motion>", self.draw)
        
        

        # drag = Label(self.window, text = "Drag the mouse to draw")
        # drag.grid(row = 2, column = 1)
# 
        self.clear = Button(self.window, text = "Clear", command=self.clear)
        self.clear.pack()
        
        self.canvas.pack()
        self.window.mainloop()


    def draw(self, event):
        self.x1 = event.x - 10
        self.y1 = event.y - 10

        self.x2 = event.x + 10
        self.y2 = event.y + 10

        self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill = "black")


    def clear(self):
        self.canvas.delete("all")

def main():
    window = Tk()
    p = paint(window)


main()