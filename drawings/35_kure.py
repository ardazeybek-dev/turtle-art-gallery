# Tel Küre
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#000208")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

R = 280
ax = m.radians(25)
ay = m.radians(20)


def project(lat, lon):
    x = m.cos(lat) * m.cos(lon)
    y = m.sin(lat)
    z = m.cos(lat) * m.sin(lon)
    x, z = x * m.cos(ay) + z * m.sin(ay), -x * m.sin(ay) + z * m.cos(ay)
    y, z = y * m.cos(ax) - z * m.sin(ax), y * m.sin(ax) + z * m.cos(ax)
    return x * R, y * R, z


def path(points):
    p.penup()
    for x, y, z in points:
        p.pencolor("#3df5ff" if z < 0 else "#173a52")
        p.width(2 if z < 0 else 1)
        p.goto(x, y)
        p.pendown()
    s.update()


for i in range(1, 12):
    lat = -m.pi / 2 + m.pi * i / 12
    path([project(lat, 2 * m.pi * j / 90) for j in range(91)])
for i in range(18):
    lon = m.pi * i / 18
    path([project(-m.pi + 2 * m.pi * j / 90, lon) for j in range(91)])

t.done()
