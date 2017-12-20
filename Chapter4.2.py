import turtle

def make_squares(turt,size,num):
    """
    makes cocentric squares. size is the size of the
    inner most and also half the distance between squares,
    num is the number of squares
    """

    origSize = size
    for j in range(num):
        turt.pendown()
        
        for i in range(4):
            turt.forward(size)
            turt.left(90)
        turt.penup()
        turt.backward(origSize/2)
        turt.right(90)
        turt.forward(origSize/2)
        turt.left(90)
        size = size + origSize
        

wn = turtle.Screen()
wn.bgcolor("lightgreen")

stef=turtle.Turtle()
stef.color("hotpink")
stef.pensize(3)
stef.speed(10)


make_squares(stef,20,5)