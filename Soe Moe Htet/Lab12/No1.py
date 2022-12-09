class Point():
    def __init__(self, x = 0.00, y = 0.00):
        self.x = x
        self.y = y

    def printInfo(self):
        print(f"Position: {self.x}, {self.y};")

class Circle(Point):
    def __init__(self, x=0, y=0, radius = 0.00):
        super().__init__(x = x, y = y)
        self.radius = radius

    def area(self):
        self.Area = 3.142 * self.radius * self.radius
        return self.Area

    def printInfo(self):
        print(f"Position: {self.x}, {self.y}; Radius: {self.radius}; Area: {self.area()}")
def main():

    p = Circle(0, 10, 10)
    p.printInfo()

main()