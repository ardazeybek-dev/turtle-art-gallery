# Harmonograf
import turtle as t
import math as m
import colorsys

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#020206")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(1)

steps = 5000
p.penup()
for i in range(steps):
    a = i * 0.05
    x = (165 * m.sin(2.0 * a) * m.exp(-0.004 * a)
         + 140 * m.sin(3.01 * a + 1.5) * m.exp(-0.003 * a))
    y = (165 * m.sin(3.0 * a + 0.5) * m.exp(-0.004 * a)
         + 140 * m.sin(2.0 * a + 0.2) * m.exp(-0.002 * a))
    p.pencolor(colorsys.hsv_to_rgb(0.5 + 0.4 * i / steps, 0.8, 1))
    p.goto(x, y)
    p.pendown()
    if i % 60 == 0:
        s.update()

s.update()
t.done()
