# Altıgen Yıldız İpliği
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("black")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(1)

R = 300
r = R / m.sqrt(3)
n = 24
colors = ["#ff4d6d", "#ffb347", "#fff275", "#7cff9e", "#62d2ff", "#c792ff"]


def lerp(a, b, f):
    return (a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f)


def line(a, b):
    p.penup()
    p.goto(a)
    p.pendown()
    p.goto(b)


for k in range(6):
    tip = (R * m.cos(m.radians(k * 60)), R * m.sin(m.radians(k * 60)))
    left = (r * m.cos(m.radians(k * 60 - 30)), r * m.sin(m.radians(k * 60 - 30)))
    right = (r * m.cos(m.radians(k * 60 + 30)), r * m.sin(m.radians(k * 60 + 30)))
    p.pencolor(colors[k])
    for i in range(n + 1):
        f = i / n
        line(lerp((0, 0), left, f), lerp(left, tip, f))
        line(lerp((0, 0), right, f), lerp(right, tip, f))
        line(lerp(left, tip, f), lerp(tip, right, f))
        s.update()

t.done()
