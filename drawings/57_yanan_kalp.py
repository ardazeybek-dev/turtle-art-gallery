# Yanan Kalp
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#0a0200")
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


p.penup()
p.goto(0, -20)
for size, col in [(620, "#160500"), (460, "#260900"), (300, "#3a0e00")]:
    p.dot(size, col)
s.update()

for cx, w, h, lean in [(-95, 110, 200, -0.35), (95, 110, 200, 0.35), (0, 150, 290, 0)]:
    for scale, col in [(1, "#d00000"), (0.75, "#ff6d00"), (0.5, "#ffba08"), (0.25, "#fff3b0")]:
        flame(cx, 0, w * scale, h * scale + 20, col, lean)
    s.update()

size = 11
p.color("#ffb703", "#c1121f")
p.width(5)
p.penup()
p.goto(0, -70 + 5 * size)
p.pendown()
p.begin_fill()
for j in range(1, 121):
    a = 2 * m.pi * j / 120
    x = 16 * m.sin(a) ** 3
    y = 13 * m.cos(a) - 5 * m.cos(2 * a) - 2 * m.cos(3 * a) - m.cos(4 * a)
    p.goto(x * size, -70 + y * size)
p.end_fill()
s.update()

p.penup()
for _ in range(50):
    p.goto(random.uniform(-200, 200), random.uniform(200, 340))
    p.dot(random.choice([2, 3, 4, 5]), random.choice(["#ffba08", "#ff6d00", "#fff3b0"]))
s.update()
t.done()
