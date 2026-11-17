# Lotus
import turtle as t

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#07020c")
s.colormode(255)
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(1.2)


def petal(r):
    p.circle(r, 60)
    p.left(120)
    p.circle(r, 60)
    p.left(120)


layers = [(300, 12, 0, (255, 120, 190)),
          (215, 10, 18, (200, 120, 255)),
          (135, 8, 0, (255, 220, 240))]

for size, count, turn, rgb in layers:
    for ring in range(12, 0, -1):
        f = ring / 12
        p.pencolor(int(rgb[0] * f), int(rgb[1] * f), int(rgb[2] * f))
        for k in range(count):
            p.penup()
            p.goto(0, 0)
            p.setheading(turn + k * 360 / count - 30)
            p.pendown()
            petal(size * f)
        s.update()

p.penup()
p.goto(0, 0)
p.dot(30, (255, 200, 60))
p.dot(12, (255, 250, 220))
s.update()
t.done()
