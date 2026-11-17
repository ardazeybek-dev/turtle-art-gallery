# Hipnoz
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("black")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(2.5)

for i in range(50):
    r = 6 + i * 6.3
    cx = 30 * m.sin(i * 0.25)
    cy = 30 * m.cos(i * 0.25)
    p.pencolor("white" if i % 2 == 0 else "#ff2a6d")
    p.penup()
    p.goto(cx, cy - r)
    p.setheading(0)
    p.pendown()
    p.circle(r)
    s.update()

t.done()
