# Ay ve Deniz
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#01030c")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.penup()

CW, CH = 8, 14
FONT = ("Courier", 10, "bold")


def put(x, y, ch, col):
    p.goto(x, y)
    p.pencolor(col)
    p.write(ch, font=FONT)


for _ in range(90):
    put(random.uniform(-340, 330), random.uniform(-20, 330), random.choice([".", ".", "*", "+"]),
        random.choice(["#cfd8ff", "#ffffff", "#8090c0"]))
s.update()

R = 95
for y in range(170 + R, 170 - R - 1, -CH):
    for x in range(-R, R + 1, CW):
        d = m.hypot(x, y - 170)
        if d > R:
            continue
        crater = 0.25 * (m.sin(x * 0.09) * m.sin(y * 0.11) > 0.4)
        b = 1 - 0.5 * (d / R) ** 2 - crater
        put(x, y, "@" if b > 0.75 else "#" if b > 0.55 else "*", "#fff3c4" if b > 0.6 else "#e9d8a6")
    s.update()

for row, y in enumerate(range(-50, -340, -CH)):
    spread = 50 + row * 6
    for x in range(-340, 340, CW):
        if abs(x) < spread and random.random() < 0.75:
            put(x, y, random.choice(["=", "~", "-"]), random.choice(["#fff3c4", "#e9d8a6", "#ffe8a3"]))
        elif random.random() < 0.55:
            put(x, y, random.choice(["~", "-", "~"]), random.choice(["#1d3557", "#274c77", "#14213d"]))
    s.update()

t.done()
