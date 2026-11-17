# Pisagor Ağacı
import turtle as t

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#050a05")
s.colormode(255)
s.tracer(0)
p = t.Turtle()
p.hideturtle()

DEPTH = 10


def square(pts, depth):
    f = depth / DEPTH
    col = (int(120 * f + 40 * (1 - f)), int(70 * f + 220 * (1 - f)), int(30 * f + 90 * (1 - f)))
    p.color("#000000", col)
    p.penup()
    p.goto(pts[0])
    p.pendown()
    p.begin_fill()
    for pt in pts[1:] + pts[:1]:
        p.goto(pt)
    p.end_fill()


def tree(x1, y1, x2, y2, depth):
    dx, dy = x2 - x1, y2 - y1
    x3, y3 = x2 - dy, y2 + dx
    x4, y4 = x1 - dy, y1 + dx
    x5 = x4 + 0.5 * (dx - dy)
    y5 = y4 + 0.5 * (dx + dy)
    square([(x1, y1), (x2, y2), (x3, y3), (x4, y4)], depth)
    if depth > 4:
        s.update()
    if depth > 0:
        tree(x4, y4, x5, y5, depth - 1)
        tree(x5, y5, x3, y3, depth - 1)


tree(-55, -280, 55, -280, DEPTH)
s.update()
t.done()
