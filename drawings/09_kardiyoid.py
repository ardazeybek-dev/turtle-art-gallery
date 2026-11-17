# Kardiyoid (Çarpım Tablosu ×2)
import turtle as t
import math as m
import colorsys

s = t.Screen()
s.setup(700, 700)
s.bgcolor("black")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

N = 240
R = 300


def point(i):
    a = 2 * m.pi * i / N + m.pi
    return R * m.cos(a), R * m.sin(a)


p.pencolor("#333344")
p.penup()
p.goto(0, -R)
p.pendown()
p.circle(R, steps=120)

for i in range(N):
    p.pencolor(colorsys.hsv_to_rgb(i / N, 0.75, 1))
    p.penup()
    p.goto(point(i))
    p.pendown()
    p.goto(point(i * 2 % N))
    s.update()

t.done()
