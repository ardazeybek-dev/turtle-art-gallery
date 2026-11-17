# Papatyalar
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#08140c")
s.tracer(0)
p = t.Turtle()
p.hideturtle()


def petal(r):
    p.circle(r, 60)
    p.left(120)
    p.circle(r, 60)
    p.left(120)


def stem(x, y):
    p.penup()
    p.goto(x, -350)
    p.pendown()
    p.pencolor("#3aa655")
    p.width(6)
    p.goto(x, y)


def daisy(x, y, size, count):
    p.width(1)
    p.color("#d9d9d9", "white")
    for k in range(count):
        p.penup()
        p.goto(x, y)
        p.setheading(k * 360 / count - 30)
        p.pendown()
        p.begin_fill()
        petal(size)
        p.end_fill()
        s.update()
    c = size * 0.28
    p.penup()
    p.goto(x, y - c)
    p.setheading(0)
    p.color("#e0a100", "#ffc300")
    p.begin_fill()
    p.circle(c)
    p.end_fill()
    p.penup()
    for n in range(60):
        a = m.radians(n * 137.5)
        r = c * 0.12 * m.sqrt(n)
        p.goto(x + r * m.cos(a), y + r * m.sin(a))
        p.dot(3, "#b36b00")
    s.update()


flowers = [(-170, 40, 120, 18), (150, 130, 150, 22), (40, -120, 90, 16)]
for x, y, size, count in flowers:
    stem(x, y)
for x, y, size, count in flowers:
    daisy(x, y, size, count)

t.done()
