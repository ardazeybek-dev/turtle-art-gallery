# Katmanlı Kalp
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("black")
s.colormode(255)
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(2)

layers = 22
for i in range(layers, 0, -1):
    k = i / layers
    size = 18.5 * k
    p.pencolor(255, int(40 + 180 * (1 - k)), int(90 + 140 * (1 - k)))
    p.penup()
    for j in range(161):
        a = j / 160 * 2 * m.pi
        x = 16 * m.sin(a) ** 3
        y = 13 * m.cos(a) - 5 * m.cos(2 * a) - 2 * m.cos(3 * a) - m.cos(4 * a)
        p.goto(x * size, y * size + 30)
        p.pendown()
    s.update()

t.done()
