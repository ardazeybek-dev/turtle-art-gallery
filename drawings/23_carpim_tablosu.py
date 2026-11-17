# Çarpım Tablosu ×21
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

N = 300
k = 21
R = 310


def point(i):
    a = 2 * m.pi * i / N
    return R * m.cos(a), R * m.sin(a)


for i in range(N):
    p.pencolor(colorsys.hsv_to_rgb(i / N, 0.7, 1))
    p.penup()
    p.goto(point(i))
    p.pendown()
    p.goto(point(i * k % N))
    if i % 3 == 0:
        s.update()

s.update()
t.done()
