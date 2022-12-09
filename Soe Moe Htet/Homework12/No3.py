import turtle as t
SIZE = 15
POINT_SIZE = SIZE 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        t.penup()
        t.setpos(self.x * POINT_SIZE, self.y * POINT_SIZE)
        t.pendown()

        t.fillcolor("red")
        t.begin_fill()
        t.circle(2)
        t.end_fill()
        t.penup()

    def print_properties(self):
        return f"x = {self.x}, y = {self.y}"

class Rectangle2D(Point):
    def __init__(self, x1, y1, x2, y2):
        centerX = (x1 + x2 ) / 2
        centerY = (y1 + y2 ) / 2
        super().__init__(centerX, centerY)

        self.x1 = x1
        self.y1 = y1

        self.x2 = x2
        self.y2 = y2

    def draw(self):
        t.pu()
        # left top point (x1)
        t.setpos(self.x1 * SIZE, self.y2 * SIZE)  

        t.pendown()
        t.goto(self.x2 * SIZE, self.y2 * SIZE)
        
        t.right(90)
        t.goto(self.x2 * SIZE, self.y1 * SIZE)
        t.right(90)
        t.goto(self.x1 * SIZE, self.y1 * SIZE)
        t.right(90)
        t.goto(self.x1 * SIZE, self.y2 * SIZE)

    

    def getWidth(self):
        return self.x1 - self.x2

    def getHeight(self):
        return self.y1 - self.y2

def getRectangle(points):
    pointList = points.split(" ")
    count = 0
    x = []
    y = []
    checkodd = True
    checkeven = False

    for i in pointList:
        if (checkodd == True):
            x.append(float(i))
            checkeven = True
            checkodd = False

        elif(checkeven == True):
            y.append(float(i))
            checkeven = False
            checkodd = True
    
    minX, maxX = find_max_min(x)
    minY, maxY = find_max_min(y)
    
    if len(x) < len(y):
        iterationpoint = len(x)
    else:
        iterationpoint = len(y)

    for i in range(iterationpoint):
        point = Point(x[i], y[i])
        point.draw()

    r = Rectangle2D(maxX, maxY, minX, minY)
    r.draw()

    print(f"The bounding rectangle is centered at ({r.print_properties()}) with width {r.getWidth()} and height {r.getHeight()}")

def find_max_min(point = []):
    min = point[0]
    for i in point:
        if (i < min):
            min = i

    max = point[0]
    for i in point:
        if (i > max):
            max = i

    return min, max

def main():

    r = input("Enter points: ")
    getRectangle(r)

    t.done()
main()