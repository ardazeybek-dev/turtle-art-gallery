# ASCII Kalp
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#0a0004")
s.colormode(255)
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.penup()

CHARS = ".:-=+*#%@"
CW, CH = 7, 12


def shape(x, y):
    u = x / 260
    v = (y + 20) / 260
    return (u * u + v * v - 1) ** 3 - u * u * v ** 3


for y in range(300, -320, -CH):
    for x in range(-330, 331, CW):
        f = shape(x, y)
        if f > 0:
            continue
        depth = min(1.0, (-f) ** 0.3)
        spot = max(0.0, 1 - m.hypot(x + 110, y - 120) / 170)
        b = min(1.0, 0.25 + 0.6 * depth + 0.5 * spot)
        ch = CHARS[min(8, int(b * 9))]
        p.goto(x, y)
        p.pencolor(255, int(30 + 200 * spot), int(70 + 150 * spot))
        p.write(ch, font=("Courier", 9, "bold"))
    s.update()

t.done()
