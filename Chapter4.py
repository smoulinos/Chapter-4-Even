import turtle
def make_square(turt,sz):
    """
    makes a square
    turt is turtle, sz is the length of the square's side
    """
    for i in range(4):
            turt.forward(sz)
            turt.left(90)


wn = turtle.Screen()
wn.bgcolor("lightgreen")

stef=turtle.Turtle()
stef.color("hotpink")
stef.pensize(3)
stef.speed(10)

#we're using two variables for size,
#original_size stayes the same in order to keep the spacing the same
#size increase by orginal_size with each repitition
orginal_size = 20
size = orginal_size
for i in range(5):
    stef.pendown()
    make_square(stef,size)
    stef.penup()
    stef.backward(orginal_size/2)
    stef.right(90)
    stef.forward(orginal_size/2)
    stef.left(90)
    size = size + orginal_size
