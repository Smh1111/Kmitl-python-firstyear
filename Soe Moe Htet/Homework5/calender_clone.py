from locale import normalize
from tkinter.font import BOLD
import turtle as t
t.speed(0)
arr = ["Su","Mo","Tu","We","Th","Fr","Sa"]

def month(mth_no,startDay, numberOfDays, a = 6, b = 7 ):
    #for month tile
    for mth_tt in range(2):
        t.fd(280)
        t.right(90)
        t.fd(20)
        t.right(90)

    t.right(90)
    t.fd(20)
    t.left(90)
    t.write("  Month#{}".format(mth_no),align="left")
    #for date header
    for cols in range(len(arr)):
        for i in range(2):
            t.fd(40)
            t.right(90)
            t.fd(20)
            t.right(90)
        #to write the content inside the cell
        t.pu()
        t.right(45)
        t.fd(25)
        t.left(45)
        t.pd()
        t.write(arr[cols])
        t.pu()
        t.right(45)
        t.fd(-25)
        t.left(45)
        t.pd()
        #labeling a cell ends here 
        t.fd(40)
    t.fd(-280)
    t.pu()
    t.right(90)
    t.fd(20)
    t.left(90)
    t.pd()
    #month body 
    c = 0
    day = 0
    for rows in range(a):
        for cols in range(b):
            for i in range(2):
                t.fd(40)
                t.right(90)
                t.fd(20)
                t.right(90)
            c+=1
            if c >= startDay and c<=numberOfDays:
                day+=1
                #to write the content inside the cell
                t.pu()
                t.right(45)
                t.fd(25)
                t.left(45)
                t.pd()
                t.write(day)
                t.pu()
                t.right(45)
                t.fd(-25)
                t.left(45)
                t.pd()
                #labeling a cell ends here 
            t.fd(40)
            
        t.fd(-280)
        t.pu()
        t.right(90)
        t.fd(20)
        t.left(90)
        t.pd()

t.pu()
t.goto(-750,370)
t.pd()
t.write("2022 CALENDER",font=("Verdana",15,"normal"))
#--------Month 1---------#
t.pu()
t.goto(-750,350)
t.pd()
month(1,7,37)
#--------Month 2---------#
t.pu()
t.goto(-750,90)
t.pd()
month(2,3,30, a = 5, b = 7 )
#--------Month 3---------#
t.pu()
t.goto(-750,-170)
t.pd()
month(3,3,33, a = 5, b = 7 )

#--------Month 4--------#
t.pu()
t.goto(-400,350)
t.pd()
month(4,6,35, a = 5, b = 7 )
#--------Month 5---------#
t.pu()
t.goto(-400,90)
t.pd()
month(5,1,31, a = 5, b = 7 )
#--------Month 6---------#
t.pu()
t.goto(-400,-170)
t.pd()
month(6,4,33, a = 5, b = 7 )

#--------Month 7---------#
t.pu()
t.goto(-50,350)
t.pd()
month(7,6,36)
#--------Month 8---------#
t.pu()
t.goto(-50,90)
t.pd()
month(8,2,32, a = 5, b = 7 )
#--------Month 9---------#
t.pu()
t.goto(-50,-170)
t.pd()
month(9,5,34, a = 5, b = 7 )

#--------Month 10--------#
t.pu()
t.goto(300,350)
t.pd()
month(10,7,37)
#--------Month 11---------#
t.pu()
t.goto(300,90)
t.pd()
month(11,3,32, a = 5, b = 7 )
#--------Month 12---------#
t.pu()
t.goto(300,-170)
t.pd()
month(12,5,35, a = 5, b = 7 )
t.done()