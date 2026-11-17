# Ateş Püskürten Ejderha
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#0a0a1a")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

FIRE = ["#d00000", "#e85d04", "#ff8800", "#ffba08", "#fff3b0"]


def body(u):
    return -310 + 480 * u, 80 * m.sin(u * 2.5 * m.pi) - 30


def direction(u):
    dx, dy = 480, 200 * m.pi * m.cos(u * 2.5 * m.pi)
    d = m.hypot(dx, dy)
    return dx / d, dy / d


def radius(u):
    return 6 + 30 * u ** 0.8


def polygon(pts, pen, fill, width=2):
    p.color(pen, fill)
    p.width(width)
    p.penup()
    p.goto(pts[0])
    p.pendown()
    p.begin_fill()
    for pt in pts[1:] + pts[:1]:
        p.goto(pt)
    p.end_fill()


def line(pts, col, width):
    p.pencolor(col)
    p.width(width)
    p.penup()
    for pt in pts:
        p.goto(pt)
        p.pendown()


p.penup()
for _ in range(90):
    p.goto(random.uniform(-350, 350), random.uniform(-350, 350))
    p.dot(random.choice([1, 2, 3]), "#ffe8a3")
s.update()

for u in (0.35, 0.72):
    x, y = body(u)
    r = radius(u)
    line([(x, y), (x - 14, y - r - 30), (x - 30, y - r - 34)], "#9d0208", 9)
    for k in (-1, 0, 1):
        line([(x - 30, y - r - 34), (x - 44 + k * 4, y - r - 46 + k * 9)], "#ffd60a", 3)
s.update()

N = 80
for i in range(0, N, 3):
    u = i / N
    x, y = body(u)
    tx, ty = direction(u)
    nx, ny = -ty, tx
    r = radius(u)
    polygon([(x + nx * r * 0.6 - tx * r * 0.5, y + ny * r * 0.6 - ty * r * 0.5),
             (x + nx * (r + 18) - tx * r * 0.7, y + ny * (r + 18) - ty * r * 0.7),
             (x + nx * r * 0.6 + tx * r * 0.5, y + ny * r * 0.6 + ty * r * 0.5)],
            "#ffb703", "#ffb703", 1)
s.update()

for i in range(N):
    u = i / N
    x, y = body(u)
    r = radius(u)
    p.color("#ffba08", "#d00000" if i % 2 == 0 else "#9d0208")
    p.width(2)
    p.penup()
    p.goto(x, y - r)
    p.setheading(0)
    p.pendown()
    p.begin_fill()
    p.circle(r)
    p.end_fill()
    if i % 4 == 0:
        s.update()

for k in range(9):
    a = m.radians(160 + k * 6)
    line([(-310, -30), (-310 + 34 * m.cos(a), -30 + 34 * m.sin(a))], FIRE[k % 5], 3)

for i in range(6):
    line([(150 - j * 9, 45 + i * 9 + 10 * m.sin(j * 0.6 + i)) for j in range(9)],
         "#ff8800", 3)
line([(162, 80), (140, 120), (118, 150)], "#ffd60a", 6)
line([(180, 85), (168, 125), (152, 162)], "#ffd60a", 6)
s.update()

p.penup()
p.goto(170, 10)
p.color("#ffba08", "#d00000")
p.width(2)
p.pendown()
p.begin_fill()
p.circle(40)
p.end_fill()
polygon([(195, 75), (262, 62), (262, 44), (200, 40)], "#ffba08", "#d00000")
polygon([(195, 30), (250, 18), (244, 6), (185, 12)], "#ffba08", "#9d0208")
for x in (212, 228, 244):
    polygon([(x, 43), (x + 5, 33), (x + 10, 43)], "white", "white", 1)
p.penup()
p.goto(254, 56)
p.dot(6, "black")
p.goto(186, 68)
p.dot(18, "#ffd60a")
p.dot(7, "black")
line([(172, 82), (200, 80)], "#ffd60a", 3)
line([(258 + j * 4, 60 + 18 * m.sin(j * 0.35) + j * 1.5) for j in range(21)], "#ffd60a", 2)
line([(240 + j * 4, 8 - 14 * m.sin(j * 0.4) - j * 2) for j in range(21)], "#ffd60a", 2)
s.update()

for k in range(46):
    a = m.radians(random.uniform(-28, 14))
    ln = random.uniform(30, 82)
    col = random.choice(FIRE)
    line([(264, 30), (264 + ln * m.cos(a), 30 + ln * m.sin(a))], col, 3)
    p.dot(random.choice([5, 7, 9]), col)
    if k % 6 == 0:
        s.update()

s.update()
t.done()
