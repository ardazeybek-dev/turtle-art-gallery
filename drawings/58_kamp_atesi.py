# Kamp Ateşi
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#050200")
s.tracer(0)
p = t.Turtle()
p.hideturtle()


def flame(cx, by, w, h, col, lean=0.0):
    p.color(col, col)
    p.penup()
    p.goto(cx, by + h)
    p.begin_fill()
    for i in range(1, 61):
        a = 2 * m.pi * i / 60
        y = h * (m.cos(a) + 1) / 2
        x = w * m.sin(a) * m.sin(a / 2) ** 2
        x += lean * (y / h) ** 2 * w + 0.12 * w * m.sin(y / h * 3 * m.pi)
        p.goto(cx + x, by + y)
    p.end_fill()


def stones(front):
    p.penup()
    for k in range(18):
        a = 2 * m.pi * k / 18
        if (m.sin(a) < 0) == front:
            p.goto(200 * m.cos(a), -215 + 30 * m.sin(a))
            p.dot(34, "#3d3d3d")
            p.dot(24, "#5a5a5a")


p.penup()
p.goto(0, -60)
for size, col in [(640, "#120400"), (460, "#200800"), (300, "#331000")]:
    p.dot(size, col)
stones(False)
s.update()

for (x1, y1, x2, y2) in [(-180, -235, 170, -165), (-170, -165, 180, -235)]:
    for width, col in [(28, "#3b1f0b"), (18, "#7f4a1f")]:
        p.width(width)
        p.pencolor(col)
        p.penup()
        p.goto(x1, y1)
        p.pendown()
        p.goto(x2, y2)
s.update()

for cx, w, h, lean in [(-80, 100, 210, -0.4), (80, 100, 210, 0.4), (0, 160, 340, 0)]:
    for scale, col in [(1, "#d00000"), (0.75, "#ff6d00"), (0.5, "#ffba08"), (0.25, "#fff3b0")]:
        flame(cx, -210, w * scale, h * scale + 25, col, lean)
    s.update()

stones(True)
p.penup()
for _ in range(45):
    p.goto(random.gauss(0, 70), random.uniform(150, 330))
    p.dot(random.choice([2, 3, 4]), random.choice(["#ffba08", "#ff6d00", "#fff3b0"]))
s.update()
t.done()
