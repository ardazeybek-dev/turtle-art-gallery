# Havai Fişek
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#03030f")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

palette = ["#ff4d6d", "#ffd23f", "#3bceac", "#5e9bff", "#ff8fd8", "#ff9f1c", "white"]

for _ in range(8):
    cx = random.uniform(-250, 250)
    cy = random.uniform(-40, 200)
    col = random.choice(palette)

    p.pencolor("#2b2b44")
    p.width(1)
    p.penup()
    p.goto(cx + random.uniform(-30, 30), -350)
    p.pendown()
    p.goto(cx, cy)

    rays = random.randint(28, 44)
    size = random.uniform(50, 100)
    p.pencolor(col)
    p.width(1.5)
    for k in range(rays):
        a = 2 * m.pi * k / rays
        ln = size * random.uniform(0.8, 1.1)
        p.penup()
        p.goto(cx + 8 * m.cos(a), cy + 8 * m.sin(a))
        p.pendown()
        p.goto(cx + ln * m.cos(a), cy + ln * m.sin(a))
        p.dot(5, col)
        p.penup()
        p.goto(cx + ln * 1.15 * m.cos(a), cy + ln * 1.15 * m.sin(a))
        p.dot(3, "white")
    s.update()

t.done()
