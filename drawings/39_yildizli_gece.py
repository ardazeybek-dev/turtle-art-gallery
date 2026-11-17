# Yıldızlı Gece
import turtle as t
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#0b1026")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.penup()

for _ in range(220):
    p.goto(random.uniform(-350, 350), random.uniform(-120, 350))
    p.dot(random.choice([1, 2, 2, 3]), random.choice(["white", "#cfd8ff", "#fff1c1"]))
s.update()


def star(x, y, size):
    p.penup()
    p.goto(x, y)
    p.setheading(72)
    p.color("#ffd166", "#ffd166")
    p.begin_fill()
    for _ in range(5):
        p.forward(size)
        p.right(144)
    p.end_fill()


for _ in range(7):
    star(random.uniform(-300, 100), random.uniform(0, 300), random.uniform(14, 26))
    s.update()

p.penup()
p.goto(220, 150)
p.color("#fff3c4", "#fff3c4")
p.begin_fill()
p.circle(60)
p.end_fill()
p.goto(245, 165)
p.color("#0b1026", "#0b1026")
p.begin_fill()
p.circle(56)
p.end_fill()
s.update()

p.goto(-330, 290)
p.pencolor("white")
p.width(2)
p.pendown()
p.goto(-180, 220)
p.penup()

for base, col, rough in [(-150, "#1d2547", 70), (-220, "#141a33", 50)]:
    p.goto(-350, -350)
    p.color(col, col)
    p.begin_fill()
    x = -350
    while x <= 350:
        p.goto(x, base + random.uniform(-rough, rough))
        x += 50
    p.goto(350, -350)
    p.goto(-350, -350)
    p.end_fill()
    s.update()

t.done()
