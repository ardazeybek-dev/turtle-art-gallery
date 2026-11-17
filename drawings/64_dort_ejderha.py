# Dört Ejderha
import turtle as t

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#080000")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(3)

turns = []
for _ in range(10):
    turns = turns + [1] + [-x for x in reversed(turns)]

colors = ["#d00000", "#ff7b00", "#ffba08", "#e5383b"]
for k in range(4):
    p.penup()
    p.goto(0, 0)
    p.setheading(k * 90)
    p.pendown()
    p.pencolor(colors[k])
    for i, turn in enumerate(turns):
        p.forward(9)
        p.left(90 * turn)
        if i % 40 == 0:
            s.update()
    p.forward(9)

s.update()
t.done()
