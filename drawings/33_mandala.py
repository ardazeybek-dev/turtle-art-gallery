# Mandala
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#07020f")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

colors = ["#f72585", "#b5179e", "#7209b7", "#560bad", "#480ca8",
          "#3a0ca3", "#3f37c9", "#4361ee", "#4895ef", "#4cc9f0"]

p.width(1.5)
for i in range(36):
    p.pencolor(colors[i % len(colors)])
    p.circle(140)
    p.left(10)
    s.update()

p.width(1)
for i in range(24):
    p.pencolor("#ffd6ff")
    p.circle(70, steps=6)
    p.left(15)
    s.update()

p.penup()
for i in range(48):
    a = 2 * m.pi * i / 48
    p.goto(310 * m.cos(a), 310 * m.sin(a))
    p.dot(10 if i % 2 == 0 else 5, colors[i % len(colors)])
s.update()
t.done()
