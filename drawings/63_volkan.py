# Volkan
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.colormode(255)
s.bgcolor(18, 0, 0)
s.tracer(0)
p = t.Turtle()
p.hideturtle()

p.width(11)
for y in range(350, -351, -10):
    f = (350 - y) / 700
    p.pencolor(int(18 + 56 * f), int(13 * f), 0)
    p.penup()
    p.goto(-350, y)
    p.pendown()
    p.goto(350, y)
s.update()

p.penup()
for _ in range(25):
    p.goto(random.gauss(0, 60), random.uniform(200, 320))
    p.dot(random.uniform(40, 90), random.choice([(45, 38, 38), (60, 50, 50), (35, 30, 30)]))
s.update()

p.color((20, 10, 6), (43, 26, 18))
p.width(2)
p.penup()
p.goto(-350, -350)
p.begin_fill()
for pt in [(-70, 90), (-35, 80), (35, 80), (70, 90), (350, -350)]:
    p.goto(pt)
p.end_fill()
s.update()

for k in range(6):
    start = random.uniform(-45, 45)
    side = -1 if start < 0 else 1
    for width, col in [(7, (255, 72, 0)), (2, (255, 208, 0))]:
        p.width(width)
        p.pencolor(col)
        p.penup()
        for j in range(41):
            f = j / 40
            y = 85 - f * 330
            x = start + side * f * (130 + k * 20) + 10 * m.sin(f * 9 + k)
            p.goto(x, y)
            p.pendown()
    s.update()

for n in range(90):
    a = m.radians(random.uniform(60, 120))
    v = random.uniform(30, 60)
    g = 8
    p.width(2.5)
    p.penup()
    for k in range(60):
        tt = k * 0.25
        x = v * m.cos(a) * tt
        y = 90 + v * m.sin(a) * tt - g * tt * tt / 2
        if y < -60 or abs(x) > 340 or y > 340:
            break
        p.pencolor((255, int(220 - k * 3.5) if k < 60 else 0, 0))
        p.goto(x, y)
        p.pendown()
    p.dot(6, (255, 200, 60))
    if n % 5 == 0:
        s.update()

s.update()
t.done()
