# Renkli İp Kalp
import turtle as t
import math as m
import random
import colorsys

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#000000")
s.tracer(0)
p = t.Turtle()
p.hideturtle()


def heart(a):
    x = 16 * m.sin(a) ** 3
    y = 13 * m.cos(a) - 5 * m.cos(2 * a) - 2 * m.cos(3 * a) - m.cos(4 * a)
    return x * 18, y * 18 + 30


N = 200
pts = [heart(2 * m.pi * i / N) for i in range(N)]

p.pencolor("#1f1f2e")
p.width(1)
p.penup()
for pt in pts + pts[:1]:
    p.goto(pt)
    p.pendown()
s.update()

p.width(1.4)
for k in range(110):
    i = random.randrange(N)
    j = (i + random.randint(20, 80)) % N
    (x1, y1), (x2, y2) = pts[i], pts[j]
    cx = (x1 + x2) / 2 * 0.5 + random.uniform(-60, 60)
    cy = (y1 + y2) / 2 * 0.5 + 15 + random.uniform(-60, 60)
    col = colorsys.hsv_to_rgb(random.random(), 0.75, 1)
    p.pencolor(col)
    p.penup()
    for step in range(31):
        f = step / 30
        x = (1 - f) ** 2 * x1 + 2 * (1 - f) * f * cx + f * f * x2
        y = (1 - f) ** 2 * y1 + 2 * (1 - f) * f * cy + f * f * y2
        p.goto(x, y)
        p.pendown()
    p.dot(5, col)
    p.penup()
    p.goto(x1, y1)
    p.dot(5, col)
    if k % 3 == 0:
        s.update()

s.update()
t.done()
