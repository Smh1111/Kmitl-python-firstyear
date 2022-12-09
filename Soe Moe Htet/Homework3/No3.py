
import turtle 

t = turtle.Turtle()

length = float(input("Enter length of each side in a star: "))

t.speed(6)
t.pensize(3)

t.color("red")

t.penup()
t.goto(-100, 100)
t.pendown()
t.forward(length)
t.right(-216)
t.forward(length)

t.right(-216)
t.forward(length)

t.right(-216)
t.forward(length)

t.right(-216)
t.forward(length)

turtle.done()