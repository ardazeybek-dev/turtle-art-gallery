# Kalp Spirali
import turtle as t
import math as m
import colorsys

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#050008")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(2)


def heart(cx, cy, size, turn):
    p.penup()
    for j in range(61):
        a = j / 60 * 2 * m.pi
        x = 16 * m.sin(a) ** 3 * size
        y = (13 * m.cos(a) - 5 * m.cos(2 * a) - 2 * m.cos(3 * a) - m.cos(4 * a)) * size
        rx = x * m.cos(turn) - y * m.sin(turn)
        ry = x * m.sin(turn) + y * m.cos(turn)
        p.goto(cx + rx, cy + ry)
        p.pendown()


count = 60
for i in range(count):
    f = i / count
    a = i * 0.42
    r = 25 + 270 * f
    p.pencolor(colorsys.hsv_to_rgb(0.85 + 0.25 * f, 0.75, 1))
    heart(r * m.cos(a), r * m.sin(a), 0.5 + 2.1 * f, a - m.pi / 2)
    s.update()

t.done()
