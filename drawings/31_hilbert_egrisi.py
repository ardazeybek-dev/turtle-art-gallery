# Hilbert Eğrisi
import turtle as t
import colorsys

s = t.Screen()
s.setup(700, 700)
s.bgcolor("black")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(2)

order = 6
step = 600 / (2 ** order - 1)
total = 4 ** order - 1
count = [0]


def go():
    p.pencolor(colorsys.hsv_to_rgb(count[0] / total, 0.8, 1))
    p.forward(step)
    count[0] += 1
    if count[0] % 40 == 0:
        s.update()


def hilbert(level, angle):
    if level == 0:
        return
    p.right(angle)
    hilbert(level - 1, -angle)
    go()
    p.left(angle)
    hilbert(level - 1, angle)
    go()
    hilbert(level - 1, angle)
    p.left(angle)
    go()
    hilbert(level - 1, -angle)
    p.right(angle)


p.penup()
p.goto(-300, 300)
p.pendown()
hilbert(order, 90)
s.update()
t.done()
