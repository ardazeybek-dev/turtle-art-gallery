# Kalplerden Kalp
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#0d0208")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

colors = ["#ff0a54", "#ff477e", "#ff7096", "#ff85a1", "#f9bec7", "#c9184a"]


def heart_xy(a):
    x = 16 * m.sin(a) ** 3
    y = 13 * m.cos(a) - 5 * m.cos(2 * a) - 2 * m.cos(3 * a) - m.cos(4 * a)
    return x, y


def small_heart(cx, cy, size, col):
    p.color(col, col)
    p.penup()
    p.goto(cx, cy + 5 * size)
    p.pendown()
    p.begin_fill()
    for j in range(1, 41):
        x, y = heart_xy(j / 40 * 2 * m.pi)
        p.goto(cx + x * size, cy + y * size)
    p.end_fill()


count = 40
for i in range(count):
    x, y = heart_xy(2 * m.pi * i / count)
    small_heart(x * 18, y * 18 + 30, 1.3, colors[i % len(colors)])
    s.update()

for i in range(18):
    x, y = heart_xy(2 * m.pi * i / 18)
    small_heart(x * 9, y * 9 + 30, 0.9, colors[(i + 2) % len(colors)])
    s.update()

small_heart(0, 30, 2.6, "#ff0a54")
s.update()
t.done()
