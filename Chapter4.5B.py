import turtle
wn=turtle.Screen()
wn.bgcolor("lightgreen")
stef = turtle.Turtle()
stef.speed(20)
stef.color("blue")
side=5
stef.penup()
stef.goto(0,0) 
stef.pendown()
stef.pensize(3)

for i in range (91):
    stef.forward(side)
    stef.left(91)
    side=side+5


stef.penup()
stef.goto(500,500)
