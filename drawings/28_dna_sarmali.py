# DNA Sarmalı
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#00050a")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

tilt = m.radians(-30)


def rot(x, y):
    return (x * m.cos(tilt) - y * m.sin(tilt),
            x * m.sin(tilt) + y * m.cos(tilt))


p.width(3)
for y in range(-360, 361, 4):
    phase = y * 0.025
    x1 = 110 * m.sin(phase)
    x2 = 110 * m.sin(phase + m.pi)
    if y % 20 == 0:
        p.penup()
        p.goto(rot(x1, y))
        p.pendown()
        p.pencolor("#ff4d8d")
        p.goto(rot(0, y))
        p.pencolor("#4dd2ff")
        p.goto(rot(x2, y))
    p.penup()
    z1 = m.cos(phase)
    p.goto(rot(x1, y))
    p.dot(8 + 4 * z1, "#ffffff" if z1 > 0 else "#7a8fa6")
    p.goto(rot(x2, y))
    p.dot(8 - 4 * z1, "#ffffff" if z1 < 0 else "#7a8fa6")
    s.update()

t.done()
