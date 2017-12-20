import turtle
wn=turtle.Screen()
bob=turtle.Turtle()
wn.bgcolor("lightgreen")
bob.color("hotpink")
def make_square (length): 
    for i in range(4):
        bob.forward(length)
        bob.left(90)
length=20
for j in range(5):
    bob.pensize(3)
    make_square(length)
    length=length+20
    bob.penup()
    bob.goto(-10 + -10*j, -10+ -10*j)
    bob.pendown()
