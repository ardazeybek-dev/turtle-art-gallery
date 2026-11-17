# Ejderha Gözü
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#080000")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

R = (300 ** 2 + 160 ** 2) / (2 * 160)


def lid(x):
    if abs(x) >= 300:
        return 0
    return m.sqrt(R ** 2 - x ** 2) - (R - 160)


p.penup()
p.goto(0, -150)
p.color("#3a0000", "#3a0000")
p.begin_fill()
p.circle(150)
p.end_fill()

p.width(2)
for i in range(360):
    a = 2 * m.pi * i / 360 + random.uniform(-0.01, 0.01)
    r2 = 150 * random.uniform(0.85, 1)
    p.penup()
    p.goto(28 * m.cos(a), 28 * m.sin(a))
    p.pendown()
    for f, col in [(0.45, "#ffd60a"), (0.75, "#ff8800"), (1, "#d00000")]:
        p.pencolor(col)
        p.goto(r2 * f * m.cos(a), r2 * f * m.sin(a))
    if i % 12 == 0:
        s.update()

p.penup()
p.color("black", "black")
p.goto(0, -140)
p.begin_fill()
for j in range(1, 81):
    y = -140 + 280 * j / 80
    p.goto(22 * m.cos(y / 140 * m.pi / 2), y)
for j in range(1, 81):
    y = 140 - 280 * j / 80
    p.goto(-22 * m.cos(y / 140 * m.pi / 2), y)
p.end_fill()
p.goto(-50, 60)
p.dot(18, "white")
s.update()

for width, col in [(14, "#2a0002"), (6, "#9d0208")]:
    p.width(width)
    p.pencolor(col)
    for sign in (1, -1):
        p.penup()
        for x in range(-300, 301, 6):
            p.goto(x, sign * lid(x))
            p.pendown()
    s.update()

p.width(3)
for sign in (1, -1):
    for row in range(5):
        for k in range(16):
            x = -330 + k * 44 + (22 if row % 2 else 0)
            y = sign * (lid(x) + 34 + row * 38)
            if abs(y) > 330 or abs(x) > 330:
                continue
            p.pencolor("#9d0208" if (row + k) % 2 else "#6a040f")
            p.penup()
            p.goto(x - 14, y)
            p.setheading(-90 if sign > 0 else 90)
            p.pendown()
            p.circle(14 * sign, 180)
        s.update()

t.done()
