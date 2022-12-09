
import turtle

x1, y1 = eval(input("Enter x1 and y1 for point 1: "))
x2, y2 = eval(input("Enter x2 and y2 for point 2: "))
x3, y3 = eval(input("Enter x3 and y3 for point 3: "))


turtle.pensize(6)

Area = Triange_Area = abs((0.5)*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
# Display two points, point 1 and point 2 and the connecting line
turtle.penup()
turtle.goto(x1, y1) # Move to (x1, y1)
turtle.pendown()

turtle.goto(x2, y2) # Draw a line to (x2, y2)

turtle.goto(x3, y3)
turtle.goto(x1, y1)

turtle.penup()
if(y1 <= y2 and y1 <= y3):
    100,
    turtle.goto(x1, y1 - 50)
    style = ('Courier', 30, 'italic')
    turtle.write(Area, font=style,  align='left')

elif(y2 <= y1 and y2 <= y3):
    
    turtle.goto(x2 - 50, y2 - 50)
    style = ('Courier', 30, 'italic')
    turtle.write(Area, font=style,  align='left')

elif(y3 <= y1 and y1 <= y2):
    
    turtle.goto(x3 - 50, y3 - 50)
    style = ('Courier', 30, 'italic')
    turtle.write(Area, font=style,  align='left')

turtle.done()