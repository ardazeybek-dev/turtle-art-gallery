# Galaksi
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#02010a")
s.colormode(255)
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.penup()

for _ in range(250):
    p.goto(random.uniform(-350, 350), random.uniform(-350, 350))
    p.dot(random.choice([1, 1, 2, 3]), "#c8c8ff")

arms = 4
for i in range(500):
    for arm in range(arms):
        r = i * 0.62
        a = m.radians(arm * 360 / arms + i * 0.9) + random.gauss(0, 0.18)
        x = r * m.cos(a) + random.gauss(0, 6)
        y = r * m.sin(a) + random.gauss(0, 6)
        f = min(1, r / 300)
        p.goto(x, y)
        p.dot(random.uniform(1.5, 4.5) * (1.4 - f),
              (int(255 - 150 * f), int(220 - 120 * f), 255))
    if i % 10 == 0:
        s.update()

p.goto(0, 0)
for size, col in [(70, "#2a1a5e"), (45, "#6b4fd8"), (25, "#e8d8ff"), (10, "white")]:
    p.dot(size, col)
s.update()
t.done()
