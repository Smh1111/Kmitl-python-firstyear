import turtle as t

def turtle_direction(x):
    t.forward(x)
    t.left(90)
    t.forward(x*2)
    t.left(90)
    t.forward(x*2)
    t.left(90)
    t.forward(x*2)
    t.left(90)
    t.forward(x)
    t.right(90)

def draw_square(diameter):
    radius = diameter / 2
    t.penup()
    t.goto(0, 0)
    t.goto(0, 0-radius)
    t.pendown()
    turtle_direction(radius)

def draw_polygon(x, y, type=4, size = 100):
    t.goto(x,y)
    if(type == 4):
        draw_square(size)
    if(type == 5):
        t.circle(size, steps=5)
    
def main():
    draw_polygon(10,10,5, 200)

main()
