# Kırmızı Gül
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#0a0205")
s.colormode(255)
s.tracer(0)
p = t.Turtle()
p.hideturtle()


def lens(r):
    p.circle(r, 90)
    p.left(90)
    p.circle(r, 90)
    p.left(90)


p.pencolor(45, 106, 79)
p.width(8)
p.penup()
for j in range(41):
    y = -40 - j * 7.3
    p.goto(18 * m.sin(j / 40 * m.pi), y)
    p.pendown()
s.update()

p.width(2)
p.color((27, 67, 50), (64, 145, 108))
for x, y, heading, r in [(10, -150, 10, 62), (8, -235, 125, 55)]:
    p.penup()
    p.goto(x, y)
    p.setheading(heading)
    p.pendown()
    p.begin_fill()
    lens(r)
    p.end_fill()
s.update()

cx, cy = 0, 110
petals = 18
p.width(1.5)
for i in range(petals - 1, -1, -1):
    f = i / (petals - 1)
    fill = (int(255 - 133 * f), int(45 - 45 * f), int(85 - 60 * f))
    p.color((74, 0, 16), fill)
    p.penup()
    p.goto(cx, cy)
    p.setheading(i * 137.5)
    p.pendown()
    p.begin_fill()
    lens(30 + i * 6.5)
    p.end_fill()
    s.update()

p.pencolor(92, 0, 21)
p.width(2)
p.penup()
p.goto(cx, cy)
p.setheading(0)
p.pendown()
for i in range(36):
    p.circle(3 + i * 1.6, 60)
s.update()
t.done()
