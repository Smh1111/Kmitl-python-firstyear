
from abc import ABC, abstractmethod

import turtle as t
t.speed(0)
class Char(ABC):
    
    @abstractmethod
    def __init__(self, width):
        self.width = width

    @abstractmethod
    def draw(self, x, y):
        pass

    @abstractmethod
    def getWidth(self):
        return self.width

    
class Char0(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        t.penup()
        t.setpos(x, y)
        t.pendown()
        width = super().getWidth()
        t.seth(0)
        
        for _ in range(4):
            t.forward(width)
            t.left(90)

    def getWidth(self):
        return self.width

class Char1(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        t.penup()
        t.setpos(x, y)
        
        width = super().getWidth()
        t.seth(0)
        t.forward(width * 0.5)

        t.pendown()
        t.left(90)
        t.forward(width)

    def getWidth(self):
        return self.width

class Char2(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        t.penup()
        t.setpos(x, y)
        t.pendown()
        width = super().getWidth()

        t.right(90)
        t.forward(width)

        t.left(180)
        t.forward(width)

        t.right(90)
        t.forward(width * 0.5)

        t.right(90)
        t.forward(width)

        t.left(90)
        t.forward(width * 0.5)

        t.left(90)
        t.forward(width)


    def getWidth(self):
        return self.width

class Char3(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        t.penup()
        t.setpos(x, y)
        t.pendown()
        width = super().getWidth()

        t.seth(90)
        t.right(90)
        t.forward(width)

        t.left(90)
        t.forward(width * 0.5)

        t.left(90)
        t.forward(width)

        t.right(180)
        t.forward(width)

        t.left(90)
        t.forward(width * 0.5)

        t.left(90)
        t.forward(width)

    def getWidth(self):
        return self.width

class Char4(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        t.penup()
        t.setpos(x, y)
        
        width = super().getWidth()

        t.seth(90)
        t.penup()
        t.right(90)
        t.forward(width)

        t.pendown()
        t.left(90)
        t.forward(width)
        
        t.penup()
        t.left(90)
        t.forward(width)

        t.pendown()

        t.left(90)
        t.forward(width * 0.5)

        t.left(90)
        t.forward(width)


    def getWidth(self):
        return self.width

class Char5(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        t.penup()
        t.setpos(x, y)
        
        width = super().getWidth()

        t.seth(90)
        t.pendown()
        t.right(90)
        t.forward(width)

        
        t.left(90)
        t.forward(width * 0.5) 
        
        t.left(90)
        t.forward(width)

        t.right(90)
        t.forward(width * 0.5)

        t.right(90)
        t.forward(width)

    def getWidth(self):
        return self.width

class Char6(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        t.penup()
        t.setpos(x, y)
        
        width = super().getWidth()

        t.seth(90)
        t.pendown()
        t.right(90)
        t.forward(width)

        
        t.left(90)
        t.forward(width * 0.5) 
        
        t.left(90)
        t.forward(width)

        t.right(90)
        t.forward(width * 0.5)

        t.right(90)
        t.forward(width)
#
        t.penup()
        t.left(180)
        t.forward(width)
#
        t.pendown()
        t.left(90)
        t.forward(width)

    def getWidth(self):
        return self.width

class Char7(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        t.penup()
        t.setpos(x, y)
        
        width = super().getWidth()

        t.seth(90)
        
        t.right(90)
        t.forward(width)

        t.pendown()
        for _ in range(2):
            t.left(90)
            t.forward(width) 
        
        

    def getWidth(self):
        return self.width

class Char8(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        t.penup()
        t.setpos(x, y)
        
        width = super().getWidth()

        t.seth(90)
        t.pendown()
        t.right(90)
        t.forward(width)

        
        t.left(90)
        t.forward(width * 0.5) 
        
        t.left(90)
        t.forward(width)

        t.right(90)
        t.forward(width * 0.5)

        t.right(90)
        t.forward(width)
#
        t.penup()
        t.left(180)
        t.forward(width)
#
        t.pendown()
        for _ in range(3):
            t.left(90)
            t.forward(width)

        
    def getWidth(self):
        return self.width

class Char9(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        t.penup()
        t.setpos(x, y)
        
        width = super().getWidth()

        t.seth(90)
        
        t.right(90)
        t.forward(width)

        t.pendown()
        for _ in range(2):
            t.left(90)
            t.forward(width) 
        
        t.left(90)
        t.forward(width * 0.5) 

        t.left(90)
        t.forward(width) 
        

    def getWidth(self):
        return self.width
def drawNum(x):
    t.clear()

    width = 60
    numberList = return_list(x)
    print(numberList)
   
    
    key_dict = {0: Char0(width), 1: Char1(width), 2: Char2(width), 3: Char3(width), 4: Char4(width), 
           5: Char5(width), 6: Char6(width), 7: Char7(width), 8: Char8(width), 9: Char9(width)}

    X_coordinate = -600
    Y_coordinate = 0
    
    for number in numberList:
        for key in key_dict:
            if (key == number):
                key_dict[key].draw(X_coordinate, Y_coordinate)
                X_coordinate += 70



def return_list(number):
    
    sum = 0
    list = []
    while(number != number // 10):   
        list.append(number % 10)
        number = number // 10

    list.reverse()

    return list



def main():
    ch0 = Char0(60)
    ch1 = Char1(60)
    ch2 = Char2(60)
    ch3 = Char3(60)
    ch4 = Char4(60)
    ch5 = Char5(60)
    ch6 = Char6(60)
    ch7 = Char7(60)
    ch8 = Char8(60)
    ch9 = Char9(60)

    ch0.draw(-600, 0)
    ch1.draw(-600 + (70 * 1) , 0)
    ch2.draw(-600 + (70 * 2) , 0)
    ch3.draw(-600 + (70 * 3) , 0)
    ch4.draw(-600 + (70 * 4) , 0)
    ch5.draw(-600 + (70 * 5) , 0)
    ch6.draw(-600 + (70 * 6) , 0)
    ch7.draw(-600 + (70 * 7) , 0)
    ch8.draw(-600 + (70 * 8) , 0)
    ch9.draw(-600 + (70 * 9) , 0)

    drawNum(65011693)
    drawNum(741098974878)

   

    t.done()
main()