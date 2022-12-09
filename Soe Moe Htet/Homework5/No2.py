
import turtle as t
win_width, win_height, bg_color = 2000, 2000, 'white'

t.setup()
t.screensize(win_width, win_height, bg_color)
t.speed(0)
arr = ["Su","Mo","Tu","We","Th","Fr","Sa"]

def month(month_no, startDay, numberOfDays, a = 6, b = 7 ):
    #tile
    for _ in range(2):
        t.fd(280)
        t.right(90)
        t.fd(20)
        t.right(90)

    t.right(90)
    t.fd(20)
    t.left(90)
    t.write(f"  Month#{month_no}", align="left")
    #Heading
    for cols in range(len(arr)):
        for i in range(2):
            t.fd(40)
            t.right(90)
            t.fd(20)
            t.right(90)

        #table contents
        t.penup()
        t.right(45)
        t.fd(25)
        t.left(45)
        t.pendown()
        t.write(arr[cols])
        t.penup()
        t.right(45)
        t.fd(-25)
        t.left(45)
        t.pendown()

        # end

        t.fd(40)

    t.fd(-280)
    t.penup()
    t.right(90)
    t.fd(20)
    t.left(90)
    t.pendown()

   
    c = 0
    day = 0
    for _ in range(a):
        for cols in range(b):
            for i in range(2):
                t.fd(40)
                t.right(90)
                t.fd(20)
                t.right(90)
            c+=1
            if c >= startDay and c<=numberOfDays:
                day+=1

               
                t.penup()
                t.right(45)
                t.fd(25)
                t.left(45)
                t.pendown()
                t.write(day)
                t.penup()
                t.right(45)
                t.fd(-25)
                t.left(45)
                t.pendown()
                
                
            t.fd(40)
            
        t.fd(-280)
        t.penup()
        t.right(90)
        t.fd(20)
        t.left(90)
        t.pendown()

def draw_month(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    

def main():
        
    draw_month(-750,370)
    #1
    draw_month(-750,350)
    month(1,7,37)
    #2
    draw_month(-750,90)
    month(2,3,30, a = 5, b = 7 )
    #3
    draw_month(-750,-170)
    month(3,3,33, a = 5, b = 7 )
    #4#
    draw_month(-400,350)
    month(4,6,35, a = 5, b = 7 )
    #5
    draw_month(-400,90)
    month(5,1,31, a = 5, b = 7 )
    #6
    draw_month(-400,-170)
    month(6,4,33, a = 5, b = 7 )
    #7
    draw_month(-50,350)
    month(7,6,36)
    #8
    draw_month(-50,90)
    month(8,2,32, a = 5, b = 7 )
    #9
    draw_month(-50,-170)
    month(9,5,34, a = 5, b = 7 )
    #10#
    draw_month(300,350)
    month(10,7,37)
    #11
    draw_month(300,90)
    month(11,3,32, a = 5, b = 7 )
    #12
    draw_month(300,-170)
    month(12,5,35, a = 5, b = 7 )

    t.done()

main()