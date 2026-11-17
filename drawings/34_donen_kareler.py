# Dönen Kareler
import turtle as t
import math as m
import colorsys

s = t.Screen()
s.setup(700, 700)
s.bgcolor("black")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(1.8)

side = 600
turn = 0
step = m.radians(5)
for i in range(60):
    h = side / 2
    corners = []
    for k in range(4):
        a = turn + m.pi / 4 + k * m.pi / 2
        corners.append((h * m.sqrt(2) * m.cos(a), h * m.sqrt(2) * m.sin(a)))
    p.pencolor(colorsys.hsv_to_rgb(i / 60, 0.8, 1))
    p.penup()
    p.goto(corners[0])
    p.pendown()
    for c in corners[1:] + corners[:1]:
        p.goto(c)
    side = side / (m.cos(step) + m.sin(step))
    turn += step
    s.update()

t.done()
