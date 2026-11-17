# Seviyor, Sevmiyor
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#0b0d24")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.penup()

SIZE = 14


def rect(x1, y1, x2, y2, col):
    p.color(col, col)
    p.goto(x1, y1)
    p.begin_fill()
    p.goto(x2, y1)
    p.goto(x2, y2)
    p.goto(x1, y2)
    p.goto(x1, y1)
    p.end_fill()


def pixel(i, j, col):
    x, y = -350 + i * SIZE, -350 + j * SIZE
    rect(x, y, x + SIZE, y + SIZE, col)


sky = ["#0b0d24", "#0e1130", "#11153a", "#151a45", "#1a2050", "#1f275c"]
for j in range(8, 50):
    pixel_row = sky[min(5, (49 - j) // 7)]
    rect(-350, -350 + j * SIZE, 350, -350 + (j + 1) * SIZE, pixel_row)
s.update()

for i in range(50):
    for j in range(50):
        d = m.hypot(i - 40, j - 42)
        if d <= 3.6 and m.hypot(i - 41.5, j - 43) > 2.8:
            pixel(i, j, "#f6f1d1")
for _ in range(40):
    i, j = random.randint(0, 49), random.randint(28, 49)
    if m.hypot(i - 40, j - 42) > 5:
        pixel(i, j, random.choice(["#ffffff", "#fff3b0", "#c8d0ff"]))
s.update()

greens = ["#1b4332", "#2d6a4f", "#40916c", "#52b788"]
for i in range(50):
    for j in range(8):
        pixel(i, j, random.choice(greens))
    if random.random() < 0.5:
        pixel(i, 8, random.choice(greens[2:]))
s.update()

for j in range(9, 26):
    pixel(25 + round(m.sin(j * 0.35)), j, "#40916c")
for k in range(3):
    pixel(23 - k, 14 + k, "#52b788")
    pixel(27 + k, 18 + k, "#52b788")
s.update()

cx, cy = 25, 27
for k in range(8):
    if k == 2:
        continue
    a = 2 * m.pi * k / 8
    for r in (2, 3, 4):
        pixel(cx + round(r * m.cos(a)), cy + round(r * m.sin(a)), "#ffffff")
    s.update()
for di in range(-1, 2):
    for dj in range(-1, 2):
        pixel(cx + di, cy + dj, "#ffc300" if (di, dj) != (0, 0) else "#e09f00")
for i, j in [(33, 32), (34, 31), (37, 27), (38, 26)]:
    pixel(i, j, "#ffffff")
s.update()

p.goto(0, 250)
p.pencolor("#ff8fab")
p.write("SEVİYOR", align="center", font=("Courier", 36, "bold"))
s.update()
t.done()
