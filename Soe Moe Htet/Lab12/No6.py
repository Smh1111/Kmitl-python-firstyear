from abc import abstractmethod


class Transportation:
    @abstractmethod
    def __init__(self, start_place, end_place, distance):
        self.startplace = start_place
        self.end_place = end_place
        self.distance = distance

    @abstractmethod
    def find_cost(self):
        pass

class Walk(Transportation):
    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance)

    def find_cost(self):
        cost = 0
        return f"Cost of walking from {self.startplace} to {self.end_place} is {cost}"

class Taxi(Transportation):
    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance)

    def find_cost(self):
        cost = 40 * self.distance
        return f"Cost of Taxi from {self.startplace} to {self.end_place} is {cost}"

class Train(Transportation):
    def __init__(self, start_place, end_place, distance, no_stations):
        super().__init__(start_place, end_place, distance)
        self.no_stations = no_stations

    def find_cost(self):
        cost = 5 * self.no_stations
        return f"Cost of Train for {self.no_stations} stations from {self.startplace} to {self.end_place} is {cost}"

def main():
    print()

    walk1 = Walk("KMITL", "KMITL SCB Bank", 0.6)
    print(walk1.find_cost())

    Taxi1 = Taxi("KMITL SCB Bank", "Ladkrabang Station", 5)
    print(Taxi1.find_cost())

    Train1 = Train("Ladkrabang Station", "Payathai Station", 40, 6)
    print(Train1.find_cost())

    Taxi1 = Taxi("Payathai Station", "British Council", 3)
    print(Taxi1.find_cost())
    
    print()

main()