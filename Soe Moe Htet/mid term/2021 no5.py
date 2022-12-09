import turtle as t
size = 100 #int(input('Size of the spiral square: '))

def draw_sq(n):
    t.pu()
    t.fd(n/2)
    t.lt(90)
    t.pd()
    t.fd(n/2)
    for i in range(3):
        t.lt(90)
        t.fd(n)
    t.lt(90)
    t.fd(n/2)
    t.pu()
    t.goto(0, 0)
    t.rt(90)

def spiral_sq(s):
    while s >=5:
            draw_sq(s)
            t.lt(10)
            s *= 0.75
     
t.getscreen()
t.speed(4)
t.lt(90)
spiral_sq(size)
t.hideturtle()
t.done()