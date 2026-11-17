# Parabolik Köşeler
import turtle as t

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#050505")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

L = 300
n = 30
corners = [((-L, -L), (1, 0), (0, 1), "#ff5c8a"),
           ((L, -L), (0, 1), (-1, 0), "#ffc857"),
           ((L, L), (-1, 0), (0, -1), "#4cd4ff"),
           ((-L, L), (0, -1), (1, 0), "#9b7bff")]


def line(x1, y1, x2, y2):
    p.penup()
    p.goto(x1, y1)
    p.pendown()
    p.goto(x2, y2)


for (cx, cy), (ax, ay), (bx, by), col in corners:
    p.pencolor(col)
    for i in range(n + 1):
        d1 = 2 * L * i / n
        d2 = 2 * L * (n - i) / n
        line(cx + ax * d1, cy + ay * d1, cx + bx * d2, cy + by * d2)
        s.update()

p.pencolor("white")
for qx, qy in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
    for i in range(n + 1):
        a = L * 0.6 * i / n
        line(qx * a, 0, 0, qy * (L * 0.6 - a))
    s.update()

t.done()
