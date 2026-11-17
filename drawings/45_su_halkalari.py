# Su Halkaları
import turtle as t
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#00111c")
s.colormode(255)
s.tracer(0)
p = t.Turtle()
p.hideturtle()

drops = [(-150, 120), (170, 160), (40, -60), (-200, -200), (210, -210)]
for cx, cy in drops:
    rings = random.randint(9, 13)
    for i in range(1, rings + 1):
        f = 1 - i / (rings + 1)
        r = i * 12
        p.pencolor(int(40 + 120 * f), int(140 + 115 * f), 255)
        p.width(1 + 2.5 * f)
        p.penup()
        p.goto(cx, cy - r)
        p.setheading(0)
        p.pendown()
        p.circle(r)
        s.update()
    p.penup()
    p.goto(cx, cy)
    p.dot(10, "white")

s.update()
t.done()
