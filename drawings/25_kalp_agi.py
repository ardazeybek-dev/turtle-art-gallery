# Kalp Ağı
import turtle as t
import math as m
import colorsys

s = t.Screen()
s.setup(700, 700)
s.bgcolor("black")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(0.8)

N = 140
jump = 41


def point(i):
    a = 2 * m.pi * i / N
    x = 16 * m.sin(a) ** 3
    y = 13 * m.cos(a) - 5 * m.cos(2 * a) - 2 * m.cos(3 * a) - m.cos(4 * a)
    return x * 18, y * 18 + 35


for i in range(N):
    p.pencolor(colorsys.hsv_to_rgb(0.9 + 0.15 * i / N, 0.8, 1))
    p.penup()
    p.goto(point(i))
    p.pendown()
    p.goto(point((i + jump) % N))
    if i % 2 == 0:
        s.update()

p.pencolor("white")
p.width(2.5)
p.penup()
for i in range(N + 1):
    p.goto(point(i % N))
    p.pendown()
s.update()
t.done()
