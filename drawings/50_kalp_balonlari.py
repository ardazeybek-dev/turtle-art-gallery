# Kalp Balonları
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#0d1b2a")
s.tracer(0)
p = t.Turtle()
p.hideturtle()


def hxy(a):
    x = 16 * m.sin(a) ** 3
    y = 13 * m.cos(a) - 5 * m.cos(2 * a) - 2 * m.cos(3 * a) - m.cos(4 * a)
    return x, y


p.penup()
for _ in range(120):
    p.goto(random.uniform(-350, 350), random.uniform(-350, 350))
    p.dot(random.choice([1, 2, 2, 3]), "#dfe7ff")

colors = ["#ff0a54", "#ff477e", "#ff85a1", "#e5383b", "#ff70a6", "#c9184a", "#ff99c8"]
balloons = []
for i in range(9):
    balloons.append((-250 + i * 62 + random.uniform(-15, 15),
                     random.uniform(40, 245), random.uniform(3.0, 4.6), colors[i % 7]))

knot = (0, -270)
p.pencolor("#e0e0e0")
p.width(1.5)
for x, y, size, col in balloons:
    tipy = y - 17 * size
    p.penup()
    for j in range(31):
        f = j / 30
        p.goto(x + (knot[0] - x) * f + 8 * m.sin(f * 4 * m.pi), tipy + (knot[1] - tipy) * f)
        p.pendown()
    s.update()

for x, y, size, col in balloons:
    p.color(col, col)
    p.penup()
    p.goto(x, y + 5 * size)
    p.begin_fill()
    for j in range(1, 81):
        hx, hy = hxy(2 * m.pi * j / 80)
        p.goto(x + hx * size, y + hy * size)
    p.end_fill()
    p.goto(x - 7 * size, y + 5 * size)
    p.dot(2.6 * size, "#ffd6e0")
    s.update()

p.penup()
p.goto(knot)
p.dot(14, "#ffd166")
p.color("#ffd166", "#ffd166")
for side in (1, -1):
    p.goto(knot)
    p.begin_fill()
    p.goto(knot[0] + side * 30, knot[1] + 14)
    p.goto(knot[0] + side * 30, knot[1] - 14)
    p.goto(knot)
    p.end_fill()
s.update()
t.done()
