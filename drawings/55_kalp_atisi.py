# Kalp Atışı
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#010a04")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

p.pencolor("#06240f")
p.width(1)
for k in range(-350, 351, 35):
    for a, b in [((k, -350), (k, 350)), ((-350, k), (350, k))]:
        p.penup()
        p.goto(a)
        p.pendown()
        p.goto(b)
s.update()

beat = [(0, 0), (30, 0), (40, 15), (50, 0), (65, 0), (72, -20), (82, 150),
        (92, -60), (100, 0), (125, 0), (140, 30), (160, 0), (200, 0)]
line = []
for x0 in (-350, -150, 50):
    for dx, dy in beat:
        line.append((x0 + dx, dy))
line.append((265, 0))

for width, col in [(9, "#0b3d1a"), (4, "#1fbf4a"), (1.5, "#c8ffd6")]:
    p.width(width)
    p.pencolor(col)
    p.penup()
    for pt in line:
        p.goto(pt)
        p.pendown()
    s.update()

for size, col in [(3.2, "#5c0016"), (2.5, "#e5003d")]:
    p.color(col, col)
    p.penup()
    p.goto(292, 5 + 5 * size)
    p.begin_fill()
    for j in range(1, 61):
        a = 2 * m.pi * j / 60
        x = 16 * m.sin(a) ** 3
        y = 13 * m.cos(a) - 5 * m.cos(2 * a) - 2 * m.cos(3 * a) - m.cos(4 * a)
        p.goto(292 + x * size, 5 + y * size)
    p.end_fill()

p.penup()
p.goto(-320, 270)
p.pencolor("#1fbf4a")
p.write("72 BPM", font=("Courier", 24, "bold"))
s.update()
t.done()
