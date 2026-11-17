# Güneş Patlaması
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#030000")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

p.penup()
for size, col in [(460, "#1a0500"), (320, "#3a0d00"), (200, "#7a1d00")]:
    p.dot(size, col)
s.update()

p.width(2)
for i in range(220):
    a = 2 * m.pi * i / 220 + random.uniform(-0.01, 0.01)
    length = random.uniform(150, 330)
    p.penup()
    for j in range(13):
        r = 70 + (length - 70) * j / 12
        ang = a + 0.06 * m.sin(r * 0.05 + i)
        f = j / 12
        p.pencolor("#fff3b0" if f < 0.2 else "#ffba08" if f < 0.5 else "#ff6d00" if f < 0.8 else "#d00000")
        p.goto(r * m.cos(ang), r * m.sin(ang))
        p.pendown()
    if i % 5 == 0:
        s.update()

p.penup()
p.goto(0, 0)
for size, col in [(150, "#ff8800"), (120, "#ffba08"), (80, "#fff3b0")]:
    p.dot(size, col)
s.update()
t.done()
