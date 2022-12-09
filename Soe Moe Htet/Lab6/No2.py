


import turtle as t

t.speed(5)

def draw_square(diameter):
    radius = diameter / 2
    t.goto(0, 0)
    t.goto(0, 0-radius)

    t.pendown()
    t.forward(radius)
    t.left(90)
    t.forward(radius*2)
    t.left(90)
    t.forward(radius*2)
    t.left(90)
    t.forward(radius*2)
    t.left(90)
    t.forward(radius)
    t.right(90)
    
    
def draw_more_squares(x):

   
    t.penup()
    #1st square
    
    draw_square(diameter= x * 2)

    # 2nd square
   
    t.penup()
    t.goto(0, -2*x)
    
    t.pendown()
    t.left(90)
    t.fd(2*x)
    t.left(90)
    t.fd(4*x)
    t.left(90)
    t.fd(4*x)
    t.left(90)
    t.fd(4*x)
    t.left(90)
    t.fd(2*x)
    t.right(90)

    # 3rd square
    t.penup()
    t.goto(0, -3*x)
    
    t.pendown()
    t.left(90)
    t.fd(3*x)
    t.left(90)
    t.fd(6*x)
    t.left(90)
    t.fd(6*x)
    t.left(90)
    t.fd(6*x)
    t.left(90)
    t.fd(3*x)
    t.right(90)

    # 4th square
    t.penup()
    t.goto(0, -4*x)
    
    t.pendown()
    t.left(90)
    t.fd(4*x)
    t.left(90)
    t.fd(8*x)
    t.left(90)
    t.fd(8*x)
    t.left(90)
    t.fd(8*x)
    t.left(90)
    t.fd(4*x)
    
    t.left(90)
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.right(90)
    t.forward(4*x)
    t.goto(0,0)
    t.left(90)
    t.forward(4*x)
    t.goto(0,0)
    t.left(90)
    t.forward(4*x)
    t.goto(0,0)
    t.left(90)
    t.forward(4*x)
    t.goto(0,0)
    t.left(90)

def main():
    t.penup()
    draw_more_squares(80)
    t.done()
    
       
main()