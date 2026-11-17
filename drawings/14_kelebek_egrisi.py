# Kelebek Eğrisi
import turtle as t
import math as m
import colorsys

s = t.Screen()
s.setup(700, 700)
s.bgcolor("black")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(2)

steps = 3000
p.penup()
for i in range(steps + 1):
    a = i / steps * 12 * m.pi
    r = m.exp(m.sin(a)) - 2 * m.cos(4 * a) + m.sin((2 * a - m.pi) / 24) ** 5
    x = r * m.sin(a) * 62
    y = r * m.cos(a) * 62 - 30
    p.pencolor(colorsys.hsv_to_rgb((0.75 + 0.35 * i / steps) % 1, 0.7, 1))
    p.goto(x, y)
    p.pendown()
    if i % 50 == 0:
        s.update()

s.update()
t.done()
