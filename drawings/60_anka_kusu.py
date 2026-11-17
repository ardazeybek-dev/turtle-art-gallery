# Anka Kuşu
import turtle as t
import math as m
import colorsys

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#0d0204")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(1.2)


def line(a, b):
    p.penup()
    p.goto(a)
    p.pendown()
    p.goto(b)


for side in (1, -1):
    for i in range(70):
        f = i / 69
        ang = m.radians(80 - 100 * f)
        R = 200 + 110 * m.sin(f * m.pi) + 14 * m.sin(f * 16 * m.pi)
        edge = (side * R * m.cos(ang), 40 + R * m.sin(ang))
        anchor = (side * 8, 60 - 100 * f)
        p.pencolor(colorsys.hsv_to_rgb(0.13 * (1 - f), 1, 1))
        line(anchor, edge)
        p.pencolor(colorsys.hsv_to_rgb(0.15, 0.4 + 0.4 * f, 1))
        line(anchor, (anchor[0] + (edge[0] - anchor[0]) * 0.55,
                      anchor[1] + (edge[1] - anchor[1]) * 0.55))
        if i % 3 == 0:
            s.update()

p.width(3)
for k in range(7):
    base = m.radians(-90 + (k - 3) * 11)
    p.pencolor(colorsys.hsv_to_rgb(0.02 + 0.02 * k, 1, 1))
    p.penup()
    for j in range(41):
        d = j * 6.5
        a = base + 0.25 * m.sin(j * 0.12) * (1 if k % 2 else -1)
        p.goto(d * m.cos(a), -40 + d * m.sin(a))
        p.pendown()
    p.dot(20, "#ff6d00")
    p.dot(9, "#ffd60a")
    s.update()

p.penup()
for y in range(-40, 70, 6):
    p.goto(0, y)
    p.dot(30 - (y + 40) * 0.08, "#ff7b00")
p.goto(0, 85)
p.dot(36, "#ffb703")
p.color("#ffd60a", "#ffd60a")
p.begin_fill()
p.goto(26, 80)
p.goto(12, 72)
p.goto(0, 85)
p.end_fill()
p.goto(4, 92)
p.dot(7, "black")
p.pencolor("#ffd60a")
p.width(3)
for x, y in [(-16, 140), (0, 152), (16, 140)]:
    line((0, 100), (x, y))
    p.dot(9, "#ff6d00")
s.update()
t.done()
