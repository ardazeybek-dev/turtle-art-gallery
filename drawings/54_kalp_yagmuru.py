# Kalp Yağmuru
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#10000c")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

colors = ["#ff0a54", "#ff477e", "#ff7096", "#ff99ac", "#fbb1bd", "#c9184a", "#ff006e", "#fb5607"]


def heart(cx, cy, size, turn, col, filled):
    p.color(col, col)
    p.width(2)
    pts = []
    for j in range(61):
        a = 2 * m.pi * j / 60
        x = 16 * m.sin(a) ** 3 * size
        y = (13 * m.cos(a) - 5 * m.cos(2 * a) - 2 * m.cos(3 * a) - m.cos(4 * a)) * size
        pts.append((cx + x * m.cos(turn) - y * m.sin(turn), cy + x * m.sin(turn) + y * m.cos(turn)))
    p.penup()
    p.goto(pts[0])
    if filled:
        p.begin_fill()
    else:
        p.pendown()
    for pt in pts[1:]:
        p.goto(pt)
    if filled:
        p.end_fill()


hearts = []
for _ in range(80):
    hearts.append((random.uniform(0.4, 2.4), random.uniform(-310, 310),
                   random.uniform(-310, 310), random.uniform(-0.5, 0.5),
                   random.choice(colors), random.random() < 0.6))
hearts.sort()

for size, x, y, turn, col, filled in hearts:
    heart(x, y, size, turn, col, filled)
    s.update()

t.done()
