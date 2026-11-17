# Aşk Mektubu
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#2b0f1f")
s.tracer(0)
p = t.Turtle()
p.hideturtle()


def hxy(a):
    x = 16 * m.sin(a) ** 3
    y = 13 * m.cos(a) - 5 * m.cos(2 * a) - 2 * m.cos(3 * a) - m.cos(4 * a)
    return x, y


def heart(cx, cy, size, col):
    p.color(col, col)
    p.penup()
    p.goto(cx, cy + 5 * size)
    p.begin_fill()
    for j in range(1, 61):
        x, y = hxy(2 * m.pi * j / 60)
        p.goto(cx + x * size, cy + y * size)
    p.end_fill()


def polygon(pts, pen, fill, width):
    p.color(pen, fill)
    p.width(width)
    p.penup()
    p.goto(pts[0])
    p.pendown()
    p.begin_fill()
    for pt in pts[1:] + pts[:1]:
        p.goto(pt)
    p.end_fill()


polygon([(-180, -40), (180, -40), (180, 250), (-180, 250)], "#d8d8e8", "#fffdf7", 2)
p.pencolor("#c4c4d6")
p.width(2)
for y in range(190, 40, -24):
    p.penup()
    p.goto(-140, y)
    p.pendown()
    p.goto(140 if y > 60 else 40, y)
heart(110, 215, 1.0, "#ff4d6d")
s.update()

polygon([(-220, 130), (0, -20), (220, 130), (220, -160), (-220, -160)],
        "#b08968", "#f2d7b6", 3)
p.pencolor("#b08968")
for x in (-220, 220):
    p.penup()
    p.goto(x, -160)
    p.pendown()
    p.goto(0, 0)
s.update()

heart(0, -20, 3.2, "#c9184a")
p.penup()
p.goto(0, -25)
p.dot(14, "#ff4d6d")
s.update()

colors = ["#ff0a54", "#ff477e", "#ff85a1", "#ffccd5"]
for i in range(12):
    f = i / 11
    x = 60 * m.sin(f * 3 * m.pi) + (f - 0.5) * 120
    y = 250 + f * 45
    heart(x - 40 + i * 8, y - 12 * m.cos(f * m.pi), 0.6 + f * 1.1, colors[i % 4])
    s.update()

t.done()
