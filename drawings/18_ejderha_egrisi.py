# Ejderha Eğrisi
import turtle as t
import colorsys

s = t.Screen()
s.setup(700, 700)
s.bgcolor("black")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(2)

turns = []
for _ in range(12):
    turns = turns + [1] + [-x for x in reversed(turns)]

p.penup()
p.goto(172, -68)
p.pendown()
step = 6.5
for i, turn in enumerate(turns):
    p.pencolor(colorsys.hsv_to_rgb(i / len(turns), 0.85, 1))
    p.forward(step)
    p.left(90 * turn)
    if i % 30 == 0:
        s.update()
p.forward(step)

s.update()
t.done()
