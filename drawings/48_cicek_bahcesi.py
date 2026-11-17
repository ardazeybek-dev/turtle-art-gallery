# Çiçek Bahçesi
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#0b1d2a")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

p.penup()
p.goto(-230, 240)
p.dot(90, "#ffd166")
p.pencolor("#ffd166")
p.width(3)
for k in range(12):
    a = 2 * m.pi * k / 12
    p.penup()
    p.goto(-230 + 58 * m.cos(a), 240 + 58 * m.sin(a))
    p.pendown()
    p.goto(-230 + 80 * m.cos(a), 240 + 80 * m.sin(a))
s.update()

p.width(2)
for _ in range(160):
    x = random.uniform(-330, 330)
    p.pencolor(random.choice(["#2d6a4f", "#40916c", "#52b788"]))
    p.penup()
    p.goto(x, -350)
    p.pendown()
    p.goto(x + random.uniform(-15, 15), -350 + random.uniform(30, 90))
s.update()

petal_colors = ["#ff595e", "#ffca3a", "#ff8fab", "#c77dff", "#4cc9f0", "#ff924c", "white"]
for _ in range(14):
    x = random.uniform(-310, 310)
    y = random.uniform(-220, 60)
    p.pencolor("#40916c")
    p.width(4)
    p.penup()
    p.goto(x, -350)
    p.pendown()
    p.goto(x + random.uniform(-20, 20), y)
    cx, cy = p.position()
    p.penup()
    size = random.uniform(14, 26)
    count = random.choice([5, 6, 8])
    col = random.choice(petal_colors)
    for k in range(count):
        a = 2 * m.pi * k / count
        p.goto(cx + size * m.cos(a), cy + size * m.sin(a))
        p.dot(size * 1.3, col)
    p.goto(cx, cy)
    p.dot(size * 0.9, "#ffd60a" if col != "#ffca3a" else "#9c6644")
    s.update()

t.done()
