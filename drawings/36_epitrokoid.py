# Epitrokoid
import turtle as t
import math as m
import colorsys

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#030006")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(2.2)

R, r, d = 120, 36, 60
steps = 2400
p.penup()
for i in range(steps + 1):
    a = i / steps * 6 * m.pi
    x = (R + r) * m.cos(a) - d * m.cos((R + r) / r * a)
    y = (R + r) * m.sin(a) - d * m.sin((R + r) / r * a)
    p.pencolor(colorsys.hsv_to_rgb((0.55 + i / steps) % 1, 0.75, 1))
    p.goto(x * 1.4, y * 1.4)
    p.pendown()
    if i % 40 == 0:
        s.update()

s.update()
t.done()
