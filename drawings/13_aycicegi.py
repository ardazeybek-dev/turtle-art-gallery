# Ayçiçeği
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#080500")
s.colormode(255)
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.penup()

golden = 137.508
count = 900
for n in range(count):
    a = m.radians(n * golden)
    r = 10.5 * m.sqrt(n)
    f = n / count
    if f < 0.55:
        col = (int(90 + 80 * f), int(45 + 40 * f), 10)
    else:
        col = (255, int(150 + 90 * (f - 0.55) / 0.45), int(20 * f))
    p.goto(r * m.cos(a), r * m.sin(a))
    p.dot(5 + 13 * f, col)
    if n % 15 == 0:
        s.update()

s.update()
t.done()
