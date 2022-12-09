from tkinter import *
class circle:
    def __init__(self, window):
        self.canvas = Canvas(
            window, 
            width = 500, 
            height = 200, 
            bg = "white"
            )

        self.canvas.bind("<Button- 1>", self.draw)
        self.canvas.bind("<Button- 3>", self.remove)
        self.canvas.pack()
        window.mainloop()
    
    def draw(self, event):
        self.x1 = event.x 
        self.y1 = event.y 
        self.x2 = event.x + 35
        self.y2 = event.y + 35

        self.oval = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2)
        
    def remove(self, event):
        tag = self.canvas.find_closest(event.x, event.y)
        self.canvas.delete(tag)
        
def main():
    window = Tk()
    c = circle(window)

main()