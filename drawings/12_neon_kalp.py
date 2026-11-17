# Neon Kalp
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#0a0006")
s.tracer(0)
p = t.Turtle()
p.hideturtle()


def heart(scale, color, width):
    p.pencolor(color)
    p.width(width)
    p.penup()
    for j in range(181):
        a = j / 180 * 2 * m.pi
        x = 16 * m.sin(a) ** 3
        y = 13 * m.cos(a) - 5 * m.cos(2 * a) - 2 * m.cos(3 * a) - m.cos(4 * a)
        p.goto(x * scale, y * scale + 30)
        p.pendown()
    s.update()


glow = [(26, "#2a0012"), (18, "#55001f"), (12, "#99002f"),
        (7, "#ff1a55"), (3, "#ff8fb0"), (1, "white")]
for width, color in glow:
    heart(15, color, width)

for width, color in glow:
    heart(8, color, max(1, width - 3))

t.done()
