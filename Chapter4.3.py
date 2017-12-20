import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("hotpink")
def  draw_poly(t, n, sz):
    for i in range(n):
        tess.forward(n)
        tess.left(sz)
        
draw_poly(tess,8,50)
