import turtle as t
import time


t.tracer(1)
def cross(length, level):
    t.pd()
    if level > 0:
        

        for _ in range(4):
            t.fd(length)
            
            cross(length /2, level - 1)
            t.fd(-length)
            t.right(90)
    else:
        t.dot(5)
    
    


cross(100, 2)

t.done()



    