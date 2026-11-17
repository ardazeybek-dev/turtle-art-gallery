# Işıltılı Lotus Fanusu
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#020214")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.penup()


def dot(x, y, size, col):
    p.goto(x, y)
    p.dot(size, col)


for _ in range(500):
    a = random.uniform(0, 2 * m.pi)
    r = random.random() ** 0.6
    dot(260 * r * m.cos(a), -250 + 40 * r * m.sin(a), random.choice([1, 2, 2, 3]),
        random.choice(["#8d8fb8", "#c9cbe8", "#5a5c88"]))
s.update()

for k in range(220):
    a = m.pi * k / 220 * 1.15 - 0.075 * m.pi
    dot(260 * m.cos(a), -40 + 260 * m.sin(a), random.choice([2, 3]), "#5b6cff")
for lon in (-0.55, 0, 0.55):
    for k in range(80):
        a = m.pi * k / 80
        dot(260 * m.sin(lon) * m.cos(a), -40 + 260 * m.sin(a), 2, "#3a46b0")
s.update()

for k in range(90):
    f = k / 89
    dot(12 * m.sin(f * 3), -245 + 275 * f, random.choice([3, 4]), "#4cc9f0")
for side, base in [(-1, -150), (1, -110)]:
    for _ in range(160):
        a = random.uniform(0, 1)
        b = random.uniform(-1, 1) * 28 * m.sin(m.pi * a)
        along = 120 * a
        ang = m.radians(90 + side * 55)
        x = along * m.cos(ang) - b * m.sin(ang)
        y = base + along * m.sin(ang) + b * m.cos(ang)
        dot(x, y, random.choice([2, 3, 4]), random.choice(["#2ec4b6", "#4cc9f0", "#90e0ef"]))
    s.update()

for _ in range(60):
    dot(random.gauss(0, 60), random.gauss(70, 40), random.uniform(20, 45), "#1b1050")
s.update()

layers = [(9, 150, 50, 0, ["#7b2ff7", "#9d4edd", "#c77dff"]),
          (7, 120, 40, 20, ["#c77dff", "#e0aaff", "#f72585"]),
          (5, 80, 30, 0, ["#ffafcc", "#ffc8dd", "#ffffff"])]
for count, length, width, turn, cols in layers:
    for k in range(count):
        ang = m.radians(20 + turn + 140 * k / (count - 1))
        for _ in range(140):
            a = random.uniform(0, 1)
            b = random.uniform(-1, 1) * width * m.sin(m.pi * a)
            along = length * a
            x = along * m.cos(ang) - b * m.sin(ang)
            y = 30 + along * m.sin(ang) + b * m.cos(ang)
            dot(x, y, random.choice([2, 3, 4]), random.choice(cols))
        s.update()

dot(0, 40, 26, "#fff3b0")
dot(0, 40, 12, "white")
s.update()
t.done()
