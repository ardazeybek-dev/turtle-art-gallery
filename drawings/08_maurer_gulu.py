# Maurer Gülü
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#04040c")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

n, d = 6, 71
R = 300

p.pencolor("#5ec8ff")
p.width(0.8)
p.penup()
for k in range(361):
    a = m.radians(k * d)
    r = R * m.sin(n * a)
    p.goto(r * m.cos(a), r * m.sin(a))
    p.pendown()
    if k % 6 == 0:
        s.update()

p.pencolor("#ff3d77")
p.width(3)
p.penup()
for k in range(361):
    a = m.radians(k)
    r = R * m.sin(n * a)
    p.goto(r * m.cos(a), r * m.sin(a))
    p.pendown()
    if k % 6 == 0:
        s.update()

s.update()
t.done()
