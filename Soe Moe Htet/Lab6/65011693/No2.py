import turtle


N = int(input("Enter a positive integer N: "))


turtle.speed(5)
loop_count = 1

while(loop_count!= N+1):

    count = 1
    
    while(count != N+1):
        
        if(loop_count % 2 == 0 and count % 2 == 0):
            turtle.fillcolor("red")
            turtle.begin_fill()
        
        if(loop_count % 2 == 1 and count % 2 == 1):
            turtle.fillcolor("red")
            turtle.begin_fill()

        for _ in range(4):
            

            turtle.forward(100/N)
            turtle.left(90)
            
        turtle.end_fill()   
        turtle.forward(100/N)
        
        count +=1
        
    
    turtle.penup()
    turtle.goto(0, loop_count*(-100/N))
    turtle.pendown()
    loop_count +=1
turtle.done()