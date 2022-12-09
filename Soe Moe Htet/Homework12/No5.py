from abc import ABC, abstractmethod


class Basket(ABC):

    @abstractmethod
    def __init__(self, title, cost, amount):
        self.title = title
        self.cost = cost
        self.amount = amount

    @abstractmethod
    def cost_of_good(self):
        pass

class StationaryGood(Basket):
    def __init__(self, title, cost, amount):
        super().__init__(title, cost, amount)

    def cost_of_good(self):
        return self.cost * self.amount

class Magazine(Basket):
    def __init__(self, title, cost, amount):
        super().__init__(title, cost, amount)

    def cost_of_good(self):
        return self.cost * self.amount

class Book(Basket):
    def __init__(self, title, cost, amount):
        super().__init__(title, cost, amount)

    def cost_of_good(self):
        discount = 0.10
        actual_cost = self.cost * self.amount

        final_cost = actual_cost - (actual_cost * discount)
        return final_cost

class Ribbon(Basket):
    def __init__(self, title, length):
        
        super().__init__(title, 5, length)

    def cost_of_good(self):
        return self.cost * self.amount
    
        
def getTotalCost(basket):

    sum = 0

    for i in basket:
        sum += i.cost_of_good()

    print(f" Total cost = {sum}")

    return sum

def main():
    m = Magazine("Computer World", 70, 3)       # 210
    b = Book("Windows 7 for Beginners", -200, 2) # 400 - 40 = 360
    r = Ribbon("Blue", 10)                      # 50

    list = [m, b, r]
    
    result = getTotalCost(list) # Total cost = 620.0 
main()

