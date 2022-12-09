import turtle

x0, y0 = eval(input("Enter x0 and y0 for p0: "))
x1, y1 = eval(input("Enter x1 and y1 for p1: "))
x2, y2 = eval(input("Enter x2 and y2 for p2: "))


c = (x1 - x0)*(y2 - y0) - (x2 - x0)*(y1 - y0)

# mid point
mid_pointx = (x0 + x1) / 2
mid_pointy = (y0 + y1) / 2


        
if (x1 > x0):
    first_pointx = x0
    first_pointy = y0
    second_pointx = x1
    second_pointy = y1
elif(x0 > x1):
    first_pointx = x1
    first_pointy = y1
    second_pointx = x0
    second_pointy = y0

print("first_pointx, first_pointy", first_pointx, first_pointy)
print("second_pointx, second_pointy", second_pointx, second_pointy)
# Display two points, point 1 and point 2 and the connecting line
turtle.penup()
turtle.goto(x0, y0) # Move to (x1, y1)
turtle.pendown()
turtle.write("p0")
turtle.goto(x1, y1) # Draw a line to (x2, y2)
turtle.write("p1")


turtle.penup()

turtle.goto(x2, y2)

turtle.write("p2")

style = ('Courier', 12, 'bold')


if (c > 0):
    turtle.goto(x2, y2-y2-y2) 
    turtle.write("p2 is on the left side of the line from p0 to  p1.", font=style,  align='left')

elif (c == 0): 

    if (x2 >= second_pointx and y2 >= second_pointy):
        turtle.goto(x2, y2-y2-y2)
        turtle.write("p2 is on the same line from p0 to p1 and on the right side.", font=style,  align='left')  
    
    elif (x2 <= first_pointx and y2 <= first_pointy):
        turtle.goto(x2, y2-y2-y2)
        turtle.write("p2 is on the same line from p0 to p1 and on the left side.", font=style,  align='left')  
    
    else:
        turtle.goto(x2+x2, y2+y2)
        turtle.write("p2 is on the same line from p0 to p1 and It's between the p0 and p1.", font=style,  align='left')
elif (c < 0): 
    turtle.goto(x2, y2-y2-y2)
    turtle.write("p2 is on the right side of the line from p0 to p1.", font=style,  align='left')

turtle.done()