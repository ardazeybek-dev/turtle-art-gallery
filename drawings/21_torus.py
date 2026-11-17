# Torus (Simit)
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("black")
s.colormode(255)
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(1)

R, r = 190, 85
tilt = m.radians(62)


def project(u, v):
    x = (R + r * m.cos(v)) * m.cos(u)
    y = (R + r * m.cos(v)) * m.sin(u)
    z = r * m.sin(v)
    y2 = y * m.cos(tilt) - z * m.sin(tilt)
    z2 = y * m.sin(tilt) + z * m.cos(tilt)
    return x * 1.15, y2 * 1.15, z2


def shade(z):
    f = (z + R + r) / (2 * (R + r))
    return int(40 + 60 * f), int(80 + 175 * f), int(120 + 135 * f)


def ring(fixed, along_u):
    p.penup()
    for j in range(81):
        a = 2 * m.pi * j / 80
        x, y, z = project(a, fixed) if along_u else project(fixed, a)
        p.pencolor(shade(z))
        p.goto(x, y)
        p.pendown()
    s.update()


for i in range(36):
    ring(2 * m.pi * i / 36, False)
for i in range(16):
    ring(2 * m.pi * i / 16, True)

t.done()
