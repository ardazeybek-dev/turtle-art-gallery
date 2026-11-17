# Gül Eğrileri
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#060006")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

roses = [(4, 300, "#ff2e63", 3), (5, 230, "#ffb400", 2.5),
         (6, 165, "#08d9d6", 2), (7, 100, "#c77dff", 2), (3, 45, "white", 2)]

for k, size, col, w in roses:
    p.pencolor(col)
    p.width(w)
    p.penup()
    turn = m.pi / (2 * k)
    for i in range(721):
        a = i / 720 * 2 * m.pi
        r = size * m.cos(k * a)
        p.goto(r * m.cos(a + turn), r * m.sin(a + turn))
        p.pendown()
        if i % 40 == 0:
            s.update()

s.update()
t.done()
