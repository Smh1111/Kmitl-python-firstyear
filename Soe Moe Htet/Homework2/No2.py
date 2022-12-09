
import turtle 

t = turtle.Turtle()

t.speed(6)
t.pensize(3)

t.color("red")

t.penup()
t.goto(0, 0)
t.pendown()
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.forward(200)
t.right(90)
t.forward(100)

t.color("blue")
t.right(45)
t.forward(100)
t.right(90)
t.forward(100)
t.left(45)

t.color("green")
t.forward(59)
t.left(90)
t.forward(70)
t.left(90)
t.write("A house")
t.forward(130)

turtle.done()

# if(count == 4):
#     copy2 = num
#     a = 1
#     while(copy2 // 10 != 0):
# 
#         a = a * 10
#         copy2 = copy2 // 10
# 
# 
#     reverse_num = 0
#     while(num != 0):
#         reverse_num += (num % 10) * a
#         num = num // 10
#         a = a // 10
# 
# 
#     print(reverse_num)

