# Alev Spirali
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#070100")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

arms = 10
for width, col in [(12, "#6a040f"), (7, "#e85d04"), (3, "#ffba08")]:
    p.pencolor(col)
    for arm in range(arms):
        p.penup()
        for j in range(121):
            r = j * 2.6
            a = arm * 2 * m.pi / arms + r * 0.011 + 0.18 * m.sin(r * 0.045)
            p.width(max(1, width * (1 - j / 140)))
            p.goto(r * m.cos(a), r * m.sin(a))
            p.pendown()
        s.update()

p.penup()
p.goto(0, 0)
for size, col in [(80, "#e85d04"), (55, "#ffba08"), (28, "#fff3b0")]:
    p.dot(size, col)
s.update()
t.done()
