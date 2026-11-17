# Sonsuzluk
import turtle as t
import math as m
import colorsys

s = t.Screen()
s.setup(700, 700)
s.bgcolor("black")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(1.6)

for k in range(20):
    size = 330 - k * 14
    p.pencolor(colorsys.hsv_to_rgb(0.5 + k / 30, 0.8, 1))
    p.penup()
    for i in range(201):
        a = i / 200 * 2 * m.pi
        d = 1 + m.sin(a) ** 2
        p.goto(size * m.cos(a) / d, size * m.sin(a) * m.cos(a) / d)
        p.pendown()
    s.update()

t.done()
