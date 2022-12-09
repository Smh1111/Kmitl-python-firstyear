from random import randint

from turtle import *
import turtle 
radius = 200
angle = 360

def Pie_chart(list1):
    list2 = []  # duplicate number list
    list3 = []  # count list
    colors = ["red", "blue", "yellow", "cyan", "brown", "orange", "green", "purple", "lime"]
    
    # Determining which numbers are duplicating
    for i in list1:
        if i not in list2:
            list2.append(i)

   # Adding number of times into list3 
   # (count numbers from list 2 in list1)
    for i in list2:
        list3.append(list1.count(i))

    # Sum of numbers in count list
    total = 0
    for i in list3:
        total += i
    
    extent = angle / total
    penup()
    sety(-radius)
    pendown()

    for i in range(len(list3)):
        value = randint(0, len(colors)- 1) 
        fillcolor(colors[value])
        begin_fill()
        circle(radius, list3[i] * extent)
        piechart = turtle.position()
        setpos(0, 0)
        end_fill()
        setpos(piechart)   

    turtle.hideturtle()
    turtle.mainloop()
    turtle.done()

def main():
    list = [3, 1, 3, 3, 2, 3, 3, 2, 3, 2, 4, 3, 3, 3, 3, 4, 3, 3, 3, 4, 3]

    Pie_chart(list)

main()