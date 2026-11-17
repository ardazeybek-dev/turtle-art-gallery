# Yıldız Poligonları
import turtle as t
import math as m

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#05030c")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.width(2)

colors = ["#ff595e", "#ff924c", "#ffca3a", "#8ac926",
          "#52a675", "#1982c4", "#4267ac", "#6a4c93"]

for idx, n in enumerate(range(12, 4, -1)):
    R = 310 - idx * 36
    k = n // 2 - 1 if n % 2 == 0 else n // 2
    p.pencolor(colors[idx])
    turn = m.pi / 2 + idx * 0.12
    for start in range(m.gcd(n, k)):
        p.penup()
        for j in range(n // m.gcd(n, k) + 1):
            v = start + j * k
            a = turn + 2 * m.pi * v / n
            p.goto(R * m.cos(a), R * m.sin(a))
            p.pendown()
    s.update()

t.done()
