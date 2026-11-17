# Sierpinski Üçgeni
import turtle as t
import colorsys

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#020205")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(1.2)


def triangle(a, b, c):
    p.pencolor(colorsys.hsv_to_rgb((a[0] + 320) / 900, 0.8, 1))
    p.penup()
    p.goto(a)
    p.pendown()
    p.goto(b)
    p.goto(c)
    p.goto(a)


def mid(a, b):
    return (a[0] + b[0]) / 2, (a[1] + b[1]) / 2


def sierpinski(a, b, c, depth):
    if depth == 0:
        triangle(a, b, c)
        return
    sierpinski(a, mid(a, b), mid(a, c), depth - 1)
    sierpinski(mid(a, b), b, mid(b, c), depth - 1)
    sierpinski(mid(a, c), mid(b, c), c, depth - 1)
    s.update()


sierpinski((-320, -270), (320, -270), (0, 284), 6)
t.done()
