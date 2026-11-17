# Aşk Oku
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#14000b")
s.tracer(0)
p = t.Turtle()
p.hideturtle()


def hxy(a):
    x = 16 * m.sin(a) ** 3
    y = 13 * m.cos(a) - 5 * m.cos(2 * a) - 2 * m.cos(3 * a) - m.cos(4 * a)
    return x, y


def heart(cx, cy, size, pen, fill, width=1):
    p.color(pen, fill)
    p.width(width)
    p.penup()
    p.goto(cx, cy + 5 * size)
    p.pendown()
    p.begin_fill()
    for j in range(1, 121):
        x, y = hxy(2 * m.pi * j / 120)
        p.goto(cx + x * size, cy + y * size)
    p.end_fill()


for _ in range(30):
    col = random.choice(["#ff4d88", "#ff99bb", "#c9184a"])
    heart(random.uniform(-320, 320), random.uniform(-320, 320),
          random.uniform(0.3, 0.7), col, col)
s.update()

d = m.atan2(0.5, 1)
p.pencolor("#ffd166")
p.width(6)
p.penup()
p.goto(-300, -150)
p.pendown()
p.goto(60, 30)

p.width(3)
p.pencolor("#ff8fab")
for k in range(4):
    bx = -300 + k * 16
    by = bx * 0.5
    for side in (1, -1):
        ang = d + m.pi + side * 0.6
        p.penup()
        p.goto(bx, by)
        p.pendown()
        p.goto(bx + 36 * m.cos(ang), by + 36 * m.sin(ang))
s.update()

heart(0, 30, 13, "white", "#e5003d", 4)
s.update()

p.pencolor("#ffd166")
p.width(6)
p.penup()
p.goto(60, 30)
p.pendown()
p.goto(290, 145)

tip = (290 + 42 * m.cos(d), 145 + 42 * m.sin(d))
left = (290 + 20 * m.cos(d + m.pi / 2), 145 + 20 * m.sin(d + m.pi / 2))
right = (290 + 20 * m.cos(d - m.pi / 2), 145 + 20 * m.sin(d - m.pi / 2))
p.color("#ffd166", "#ffd166")
p.penup()
p.goto(left)
p.begin_fill()
p.goto(tip)
p.goto(right)
p.goto(left)
p.end_fill()
s.update()
t.done()
