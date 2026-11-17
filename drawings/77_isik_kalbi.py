# Işık Kalbi
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#05000a")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.penup()


def heart(a, r):
    x = 16 * m.sin(a) ** 3
    y = 13 * m.cos(a) - 5 * m.cos(2 * a) - 2 * m.cos(3 * a) - m.cos(4 * a)
    return x * 18 * r, (y + 2) * 18 * r + 10


for _ in range(70):
    x, y = heart(random.uniform(0, 2 * m.pi), random.uniform(0.3, 0.9))
    p.goto(x, y)
    p.dot(random.uniform(40, 80), "#1a0414")
s.update()

colors = ["#ff4d88", "#ff85a1", "#ffc2d1", "#ffffff", "#ff0a54", "#f72585"]
for k in range(2600):
    r = random.random() ** 0.25
    x, y = heart(random.uniform(0, 2 * m.pi), r)
    p.goto(x + random.gauss(0, 3), y + random.gauss(0, 3))
    p.dot(random.choice([2, 2, 3, 4]) * (0.6 + r * 0.6), random.choice(colors))
    if k % 50 == 0:
        s.update()

for _ in range(40):
    p.goto(random.uniform(-330, 330), random.uniform(-330, 330))
    p.dot(random.choice([2, 3]), "#ffd6e0")
s.update()
t.done()
