# Sekiz Yapraklı Çiçek
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#05030a")
s.colormode(255)
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(1.3)


def layer(size, turn, rings, rgb):
    for i in range(rings, 0, -1):
        f = i / rings
        p.pencolor(int(rgb[0] * f), int(rgb[1] * f), int(rgb[2] * f))
        for k in range(8):
            base = m.radians(turn + k * 45)
            p.penup()
            for j in range(-15, 16):
                phi = j / 15 * m.pi / 8
                d = size * f * max(0, m.cos(4 * phi)) ** 0.5
                p.goto(d * m.cos(base + phi), d * m.sin(base + phi))
                p.pendown()
        s.update()


layer(280, 0, 22, (235, 240, 255))
layer(200, 22.5, 18, (120, 170, 255))
layer(135, 0, 14, (255, 120, 210))
layer(75, 22.5, 10, (255, 60, 90))

p.penup()
p.goto(0, 0)
p.dot(26, "#ff0033")
p.dot(8, "white")
s.update()
t.done()
