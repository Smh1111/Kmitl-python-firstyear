from ctypes import sizeof
import turtle
from typing import Sized 

centerx= float(input("Enter the centerx: "))
centery= float(input("Enter the centerx: "))
radius = float(input("Enter the radius: "))


area = 3.142 * radius * radius

turtle.pensize(3)
turtle.penup()
turtle.goto(centerx, centery)
turtle.pendown()
turtle.circle(radius)
turtle.penup()

turtle.goto(centerx, centery + radius)
turtle.write(area, align="center")

turtle.done()