# Spirograf
import turtle as t
import math as m
import colorsys

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#020208")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(1.5)

R, r, d = 250, 90, 115
steps = 2400
p.penup()
for i in range(steps + 1):
    a = i / steps * 2 * m.pi * 9
    x = (R - r) * m.cos(a) + d * m.cos((R - r) / r * a)
    y = (R - r) * m.sin(a) - d * m.sin((R - r) / r * a)
    p.pencolor(colorsys.hsv_to_rgb(i / steps, 0.8, 1))
    p.goto(x * 1.1, y * 1.1)
    p.pendown()
    if i % 40 == 0:
        s.update()

s.update()
t.done()
