import turtle as t

HEIGHT = 20
WIDTH = 40
SIZE = 2
pos_X = -200
pos_Y = 0
k = []
t.speed(5)

def axis(highest_count, no_characters):
    
    x_axis = no_characters * WIDTH 
    y_axis = highest_count * HEIGHT 

    
    t.shape("arrow")

    # Vertical Axis
    t.penup()
    t.goto(pos_X, pos_Y)
    
    t.pendown()
    t.left(90)
    
    
    t.forward(y_axis)

    t.stamp()

    t.right(90)

    
    t.goto(pos_X, pos_Y)
    # Horizontal Axis
    #t.penup()
    #t.goto(pos_X,pos_Y)
#
    #
    #t.pendown()
    #t.right(90)
    #t.forward(x_axis*SIZE)
    #t.stamp()

    t.penup()
    

    return (x_axis , y_axis)


def draw_bar(char, text_count, i, x_axis, y_axis, length, no_characters):
    
   
    # Character bar
    t.pendown()
    
    t.forward(x_axis / (no_characters))

    t.penup()
    t.right(90)
    t.forward(20)
    t.left(180)
    t.write(char, font=("Times New Roman", 15, "bold"))
    t.forward(20)
    
    t.pendown()
    t.forward(text_count * HEIGHT)

    t.right(90)
    t.forward(10)
    t.right(90)

    t.forward(text_count * HEIGHT)


    t.right(90)
    t.forward(10)

    t.left(180)
    t.forward(10)

    if (i == length-1):
        
        t.forward(x_axis / (no_characters))
        t.stamp()
    t.penup()
    

def main():
    text = input("Enter some text: ")

    for i in text:
        if i not in k:
            k.append(i)

    no_characters = len(k)
    highest_count = 0

    for i in range(0, len(k)):
        

        if (highest_count < text.count(k[i])):
            highest_count = text.count(k[i])
        
    

    (x_axis, y_axis) = axis(highest_count, no_characters)

    
    t.goto(pos_X, pos_Y)
    
    for i in range(0, len(k)):
        

        if (highest_count < text.count(k[i])):
            highest_count = text.count(k[i])
        

        draw_bar(k[i], text.count(k[i]), i, x_axis, y_axis, len(k), no_characters)
    t.hideturtle()
    t.done()

main()