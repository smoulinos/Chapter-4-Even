import turtle
stef=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("light green")
stef.pensize(3)
stef.color("hotpink")
for i in range(5):
    for b in range(4):
        stef.forward(20)
        stef.left(90)
    stef.penup()
    stef.forward(35)
    stef.pendown()
