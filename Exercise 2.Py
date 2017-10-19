import turtle
def make_square(turt,size):
    for i in range(4):
        turt.fd(size)
        turt.left(90)
wn=turtle.Screen()
wn.bgcolor("lightgreen")
lx=turtle.Turtle()
lx.color("hotpink")
lx.pensize(3)
square_size=20
for i in range(4):
    lx.pendown()
    make_square(lx, square_size)
    lx.penup()
    lx.backward(10)
    lx.right(90)
    lx.forward(10)
    lx.left(90)
    square_size=square_size+20