import turtle
wn=turtle.Screen()
wn.bgcolor("lightgreen")
stef = turtle.Turtle()
stef.speed(20)
stef.color("hotpink")
side=5
stef.penup()
stef.goto(0,0) 
stef.pendown()
stef.pensize(3)

for i in range(5):
    stef.forward(100)
    stef.left(144)
