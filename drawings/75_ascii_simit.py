# ASCII Simit (Donut)
import turtle as t
import math

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#050505")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.penup()

W, H = 80, 40
CW, CH = 8, 14
LUM = ".,-~:;=!*#$@"
COLORS = ["#3d2a14", "#5c3d1e", "#7f5539", "#9c6644", "#b07d4f", "#c68b59",
          "#d9a066", "#e6b17e", "#f0c38e", "#f7d4a3", "#fde4bd", "#fff5e1"]

out = [[None] * W for _ in range(H)]
zbuf = [[0.0] * W for _ in range(H)]
A, B = 1.0, 0.6

for j in range(0, 628, 7):
    theta = j / 100
    for i in range(0, 628, 2):
        phi = i / 100
        c, l = math.sin(phi), math.cos(phi)
        d, f = math.cos(theta), math.sin(theta)
        e, g = math.sin(A), math.cos(A)
        h = d + 2
        D = 1 / (c * h * e + f * g + 5)
        cb, sb = math.cos(B), math.sin(B)
        tt = c * h * g - f * e
        x = int(40 + 38 * D * (l * h * cb - tt * sb))
        y = int(20 + 19 * D * (l * h * sb + tt * cb))
        N = int(8 * ((f * e - c * d * g) * cb - c * d * e - f * g - l * d * sb))
        if 0 <= y < H and 0 <= x < W and D > zbuf[y][x]:
            zbuf[y][x] = D
            out[y][x] = max(N, 0)

for y in range(H):
    for x in range(W):
        n = out[y][x]
        if n is None:
            continue
        p.goto(-320 + x * CW, 270 - y * CH)
        p.pencolor(COLORS[n])
        p.write(LUM[n], font=("Courier", 10, "bold"))
    s.update()

t.done()
