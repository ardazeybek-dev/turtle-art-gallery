# İki Kalp
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#07000a")
s.tracer(0)
p = t.Turtle()
p.hideturtle()


def heart_points(cx, cy, size, turn):
    pts = []
    for j in range(181):
        a = 2 * m.pi * j / 180
        x = 16 * m.sin(a) ** 3 * size
        y = (13 * m.cos(a) - 5 * m.cos(2 * a) - 2 * m.cos(3 * a) - m.cos(4 * a)) * size
        pts.append((cx + x * m.cos(turn) - y * m.sin(turn),
                    cy + x * m.sin(turn) + y * m.cos(turn)))
    return pts


def neon(pts, layers):
    for width, col in layers:
        p.width(width)
        p.pencolor(col)
        p.penup()
        for pt in pts:
            p.goto(pt)
            p.pendown()
        s.update()


pink = [(18, "#3d0018"), (11, "#8a0036"), (6, "#ff2e7e"), (2, "#ffc2d9")]
gold = [(18, "#3d2a00"), (11, "#8a6100"), (6, "#ffb703"), (2, "#fff1c2")]

right = heart_points(80, 10, 10.5, -0.25)
left = heart_points(-80, 10, 10.5, 0.25)
neon(right, gold)
neon(left, pink)
neon(right[100:150], gold)

p.pencolor("white")
p.width(2)
for _ in range(14):
    x, y = random.uniform(-320, 320), random.uniform(-320, 320)
    size = random.uniform(5, 11)
    for dx, dy in [(1, 0), (0, 1)]:
        p.penup()
        p.goto(x - dx * size, y - dy * size)
        p.pendown()
        p.goto(x + dx * size, y + dy * size)
s.update()
t.done()
