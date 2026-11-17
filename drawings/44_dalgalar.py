# Dalgalar
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("black")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.color("white", "black")
p.width(1.6)

for row in range(30):
    y0 = 270 - row * 19
    bumps = [(random.uniform(-90, 90), random.uniform(10, 45), random.uniform(15, 35))
             for _ in range(5)]
    pts = []
    for x in range(-260, 261, 6):
        env = m.exp(-(x / 130) ** 4)
        h = sum(b * m.exp(-((x - c) / w) ** 2) for c, b, w in bumps)
        pts.append((x, y0 + env * (h + random.uniform(0, 4))))

    p.penup()
    p.goto(pts[0])
    p.begin_fill()
    for pt in pts:
        p.goto(pt)
    p.goto(260, y0 - 4)
    p.goto(-260, y0 - 4)
    p.end_fill()

    p.goto(pts[0])
    p.pendown()
    for pt in pts:
        p.goto(pt)
    s.update()

t.done()
