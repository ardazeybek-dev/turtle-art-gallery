# Lissajous Dansı
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#000308")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(1.4)

colors = ["#00f5d4", "#00bbf9", "#9b5de5", "#f15bb5", "#fee440"]
for k, col in enumerate(colors):
    p.pencolor(col)
    phase = k * m.pi / 10
    size = 290 - k * 18
    p.penup()
    for i in range(721):
        a = i / 720 * 2 * m.pi
        p.goto(size * m.sin(3 * a + phase), size * m.sin(4 * a))
        p.pendown()
        if i % 30 == 0:
            s.update()

s.update()
t.done()
