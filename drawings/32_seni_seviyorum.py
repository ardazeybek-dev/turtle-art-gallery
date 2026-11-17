# Seni Seviyorum
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#12000a")
s.tracer(0)
p = t.Turtle()
p.hideturtle()


def heart_point(a, size, cx, cy):
    x = 16 * m.sin(a) ** 3
    y = 13 * m.cos(a) - 5 * m.cos(2 * a) - 2 * m.cos(3 * a) - m.cos(4 * a)
    return cx + x * size, cy + y * size


def heart(size, cx, cy, pen, fill):
    p.color(pen, fill)
    p.penup()
    p.goto(heart_point(0, size, cx, cy))
    p.pendown()
    p.begin_fill()
    for j in range(1, 121):
        p.goto(heart_point(j / 120 * 2 * m.pi, size, cx, cy))
    p.end_fill()


for _ in range(45):
    size = random.uniform(0.4, 1.3)
    col = random.choice(["#ff4d88", "#ff99bb", "#c9184a", "#ffccd5"])
    heart(size, random.uniform(-320, 320), random.uniform(-320, 320), col, col)
    s.update()

p.width(4)
heart(16, 0, 30, "white", "#e5003d")
s.update()

p.penup()
p.goto(0, 0)
p.pencolor("white")
p.write("Seni Seviyorum", align="center", font=("Arial", 32, "bold"))
s.update()
t.done()
