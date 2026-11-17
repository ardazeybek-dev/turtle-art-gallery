# Hiperbolik Ağ
import turtle as t
import math as m
import colorsys

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#000000")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(1)

N = 90
twist = 30


def top(i):
    a = 2 * m.pi * i / N
    return 230 * m.cos(a), 230 + 55 * m.sin(a)


def bottom(i):
    a = 2 * m.pi * i / N
    return 230 * m.cos(a), -230 + 55 * m.sin(a)


for i in range(N):
    p.pencolor(colorsys.hsv_to_rgb(0.45 + 0.4 * i / N, 0.7, 1))
    p.penup()
    p.goto(top(i))
    p.pendown()
    p.goto(bottom(i + twist))
    p.penup()
    p.goto(top(i))
    p.pendown()
    p.goto(bottom(i - twist))
    s.update()

p.pencolor("white")
p.width(2)
for ring in (top, bottom):
    p.penup()
    for i in range(N + 1):
        p.goto(ring(i))
        p.pendown()
s.update()
t.done()
