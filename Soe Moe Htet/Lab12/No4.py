from abc import abstractmethod
import turtle as t

class TwoDShape:
    def __init__():
        pass
    
    @abstractmethod
    def draw_shape(self):
        pass
    
class Line(TwoDShape):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def draw_shape(self):
        t.penup()
        t.setpos(self.x1, self.x2)
        t.pendown()
        t.setpos(self.x2, self.y2)

    
class Rectangle(TwoDShape):
    def __init__(self, x1, y1, width, height):
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height

    
    def draw_shape(self):
        t.penup()
        t.setpos(self.x1, self.y1)
        t.pendown()
        
        for _ in range(4):
            t.forward(self.width)
            t.right(90)
            t.forward(self.height)

        t.penup()
    
class Circle(TwoDShape):
    def __init__(self, x1, y1, radius):
        self.x1 = x1
        self.y1 = y1
        self.radius = radius
        
    
    def draw_shape(self):
        t.penup()
        t.setpos(self.x1, self.y1)
        t.pendown()
        t.circle(self.radius)

def main():
    t.speed(0)
    l1 = Line(10, 0, 100, 0)
    l1.draw_shape()

    r1 = Rectangle(-300, 300, 100, 50)
    r1.draw_shape()


    c1 = Circle(0, -300, 50)
    c1.draw_shape()
    t.done()
main()