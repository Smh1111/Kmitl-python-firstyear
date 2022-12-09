
from calendar import month
import turtle
win_width, win_height, bg_color = 2000, 2000, 'white'

turtle.setup()
turtle.screensize(win_width, win_height, bg_color)


t = turtle.Turtle()

def tables(x, y):
    x = x 
    y = y
    t.goto(x, y)
    a = 1

    count = 1
    while(count != 4):
        
        row = 8
        column = 7
        row_count = 1

        
        t.speed(0)

        t.pendown()

        row_length = 200
        month_table_number = count
        t.write(f"   Month#{month_table_number}" , False , "left" , "Arial 12" )
        for _ in range(2):    
            t.forward(row_length-row_length/row)
            t.left(90)
            t.forward(row_length/row)
            t.left(90)
    
        t.goto(x, y - row_length/row)
        #__________________________________________________________________
        column_count = 0
        arr = [" Su ", " Mo ", " Tu ", " We ", " Th ", " Fr ", " Sa "]

        while(column_count!= 7):

            t.write(arr[column_count] , False , "left" , "Arial 12" )  

            for _ in range(4): 
                t.forward(row_length/row)
                t.left(90)

            t.forward(row_length/row)
            column_count += 1

        t.penup()
        t.goto(x, y - row_length*2/row)
        t.pendown()
        
        print("numbers ", a)
      #__________________________________________________________________
        table_numbers = a # 1
#row = 8
#column = 7       
        if (count == 1):
            while(row_count!= 6):
                column_count = 1
                while(column_count != 8):

                    if (count == 1 and row_count == 1 and column_count < 7):
                            t.write(f" ", False , "left" , "Arial 12" )
                          
                    else:
                        t.write(f"  {table_numbers}", False , "left" , "Arial 12" )
                    table_numbers += 1 


                    for _ in range(4):
                        t.forward(row_length/row)
                        t.left(90)


                    t.forward(row_length/row)
                    column_count += 1

                t.penup()
                t.goto(x, y - row_length*(row_count+2)/row)
                t.pendown()
                row_count +=1

        t.penup()
        y = y - 250
        t.goto(x, y)
        
        a = table_numbers
        count += 1
        
def draw_table_numbers():
    print()

def main():

    month_table_number = 1
    t.penup()
    
    
    tables(-600, 600)
    
    t.penup()    


    turtle.done()
main()