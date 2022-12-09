class Calculator:
    def __init__(self, acc = 0.00):
        self.acc = acc
    
    def set_accumator(self, a):
        self.acc = a

    def get_accumator(self):
        return self.acc

    def add(self, x):
        self.acc = self.acc + x
    
    def subtract(self, x):
        self.acc = self.acc - x

    def multiply(self, x):
        self.acc = self.acc * x
    
    def divide(self, x):
        self.acc = self.acc / x
    
    def print_result(self):
        print(f"Result: {self.acc}")


class Sci_calc(Calculator):
    def __init__(self, acc=0):
        super().__init__(acc)

    def square(self):
        self.acc = self.acc * self.acc
    
    def exp(self, x):
        self.acc = self.acc ** x
    
    def factorial(self):
        self.acc = self.acc

    def print_result(self):
        format = "{:e}".format(self.acc)
        print(f"Result: {format}")

def main():
    c = Sci_calc()
    c.add(100)
    c.square()
    c.print_result()

main()