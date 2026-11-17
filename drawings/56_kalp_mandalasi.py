# Kalp Mandalası
import turtle as t
import math as m
import colorsys

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#0b0010")
s.tracer(0)
p = t.Turtle()
p.hideturtle()


def heart(direction, dist, size, filled=False):
    rot = direction - m.pi / 2
    ox, oy = dist * m.cos(direction), dist * m.sin(direction)
    pts = []
    for j in range(61):
        a = 2 * m.pi * j / 60
        x = 16 * m.sin(a) ** 3 * size
        y = (13 * m.cos(a) - 5 * m.cos(2 * a) - 2 * m.cos(3 * a) - m.cos(4 * a) + 17) * size
        pts.append((ox + x * m.cos(rot) - y * m.sin(rot), oy + x * m.sin(rot) + y * m.cos(rot)))
    p.penup()
    p.goto(pts[0])
    if filled:
        p.begin_fill()
    else:
        p.pendown()
    for pt in pts[1:]:
        p.goto(pt)
    if filled:
        p.end_fill()


p.width(1.6)
rings = [(12, 7.0, 0), (12, 4.6, m.pi / 12), (8, 2.6, 0)]
for count, size, offset in rings:
    for i in range(count):
        for k, scale in enumerate((1, 0.8, 0.6)):
            p.pencolor(colorsys.hsv_to_rgb((0.88 + 0.04 * k + i / count * 0.15) % 1, 0.75, 1))
            heart(offset + 2 * m.pi * i / count, 0, size * scale)
        s.update()

for i in range(24):
    col = "#ff4d88" if i % 2 == 0 else "#ffd166"
    p.color(col, col)
    heart(2 * m.pi * i / 24, 268, 1.3, True)
s.update()
t.done()
