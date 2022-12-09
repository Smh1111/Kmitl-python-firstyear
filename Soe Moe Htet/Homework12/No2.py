
import turtle as t
t.speed(0)

def RobotBattle():
    #robotList stores the list of robots in the battle

    robotList = []
    while True:
        # Clear the screen and draw the robots
        t.clear()
        for robot in robotList:
            robot.draw()

        # Display the status of each robot
        print("============= Robots =============")
        i = 0
        for robot in robotList:
            print(i, " : ")
            robot.displayStatus()
            i += 1
        print("==========================")

        # Ask user which robot to command or to create a new robot
        choice = input("Enter which robot to order, 'c' to create new robot, 'q' to quit \n")
        
        if choice == "q":
            break

        elif choice == "c":
            print("Enter which type of robots to create\n")
            robotType = input("'r' for Robot, 'm' for MedicBot, 's' for StrikerBot\n")
            if robotType == "r":
                newRobot = Robot()
            
            elif robotType == "m":
                newRobot = MedicBot()
            
            elif robotType == "s":
                newRobot = StrikerBot()
            
            robotList = robotList + [newRobot]
        
        else:
            n = int(choice)
            robotList[n].command(robotList)

        i = 0
        for robot in robotList:
            if (robot.health <= 0):
                del robotList[i]
            i += 1

class Robot(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.health = 100
        self.energy = 100

    def move(self, newX, newY):
        if (self.energy > 0):
            self.x = newX
            self.y = newY
            self.energy -= 10
        
        elif (self.energy <= 0):
            pass
        print()

    def draw(self):
        t.pu()
        t.setpos(self.x, self.y)
        
        t.pd()
        t.circle(30)


    def displayStatus(self):
        print(f" x = {self.x}, y = {self.y}, health = {self.health}, energy = {self.energy}")

    def command(self, robotList):
        print("Possible actions: move\n")
        newX = int(input("Enter new x-coordinate: "))
        newY = int(input("Enter new y-coordinate: "))
        self.move(newX, newY)

class MedicBot(Robot):
    def __init__(self):
        super().__init__()

    def heal(self, r):

        distancex = self.x - r.x
        distancey = self.y - r.y


        if (self.energy >= 20 and distancex <= 10 and distancey <= 10):
            self.energy -= 20
            r.health += 10
        else:
            pass

    def command(self, robotList):
        print("Possible actions: move, heal.\n")
        command = input("Enter 'move' for move action, 'heal' for heal action: \n")

        if (command == "move"):

            newX = int(input("Enter new x-coordinate: "))
            newY = int(input("Enter new y-coordinate: "))
            self.move(newX, newY)

        elif (command == "heal"):
            
            robot_to_heal = int(input("Choose which robot to heal: "))
            self.heal(robotList[robot_to_heal])
        
    def draw(self):
        super().draw()

        t.penup()
        t.forward(-5)

        t.left(90)
        t.forward(15)

        t.pendown()

        t.right(90)
        t.forward(10)

        for _ in range(3):
            t.left(90)
            t.forward(10)

            t.right(90)
            t.forward(10)

            t.left(90)
            t.forward(10)

        t.left(90)
        t.forward(10)

        t.right(90)
        t.forward(10)

        

class StrikerBot(Robot):
    def __init__(self):
        super().__init__()
        self.missile = 5

    def strike(self, r):
        distancex = self.x - r.x
        distancey = self.y - r.y
        if (self.energy >= 20 and self.missile > 0 and distancex <= 10 and distancey <= 10):
            self.energy -= 20
            self.missile -= 1
            r.health -= 50
        else:
            pass
    
    def displayStatus(self):
        print(f" x = {self.x}, y = {self.y}, health = {self.health}, energy = {self.energy}, missile = {self.missile}")


    def command(self, robotList):
        print("Possible actions: move, strike.\n")
        command = input("Enter 'move' for move action, 'strike' for strike action: \n")

        if (command == "move"):

            newX = int(input("Enter new x-coordinate: "))
            newY = int(input("Enter new y-coordinate: "))
            self.move(newX, newY)

        elif (command == "strike"):
           
            robot_to_strike = int(input("Choose which robot to strike: "))
            self.strike(robotList[robot_to_strike])

    def draw(self):
        super().draw()
        t.penup()
        
        t.left(90)
        t.forward(10)

        t.pendown()
        t.right(90)
        t.circle(20, 360, 4)
        

def main():
    RobotBattle()

main()