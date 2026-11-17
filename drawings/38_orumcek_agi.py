# Örümcek Ağı
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#04060a")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

spokes = 18
angles = [2 * m.pi * i / spokes + random.uniform(-0.06, 0.06) for i in range(spokes)]

p.pencolor("#dfe6f0")
p.width(1.2)
for a in angles:
    p.penup()
    p.goto(0, 0)
    p.pendown()
    p.goto(330 * m.cos(a), 330 * m.sin(a))
s.update()

p.pencolor("#aab4c3")
p.width(1)
for ring in range(1, 23):
    r = ring * 14
    p.penup()
    for i in range(spokes):
        a1 = angles[i]
        a2 = angles[(i + 1) % spokes]
        for j in range(7):
            f = j / 6
            sag = 1 - 0.08 * m.sin(m.pi * f)
            a = a1 + ((a2 - a1) % (2 * m.pi)) * f
            p.goto(r * sag * m.cos(a), r * sag * m.sin(a))
            p.pendown()
    s.update()

p.penup()
p.goto(120, 350)
p.pendown()
p.pencolor("#dfe6f0")
p.goto(120, 150)
p.penup()
p.width(2)
p.pencolor("#e63946")
for k in range(8):
    side = 1 if k < 4 else -1
    a = m.radians(side * (25 + (k % 4) * 22))
    p.goto(120, 140)
    p.pendown()
    p.goto(120 + side * 22 * m.cos(a), 140 + 18 * m.sin(a) * side)
    p.goto(120 + side * 34 * m.cos(a), 140 - 14 + 10 * m.sin(a) * side)
    p.penup()
p.goto(120, 140)
p.dot(26, "#e63946")
p.goto(120, 154)
p.dot(16, "#e63946")
s.update()
t.done()
