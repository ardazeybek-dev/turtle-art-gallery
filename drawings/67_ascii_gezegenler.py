# ASCII Gezegenler
import turtle as t
import math as m
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#02030a")
s.colormode(255)
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.penup()

CHARS = " .:-=+*#%@"
FONT = ("Courier", 9, "bold")
CW, CH = 7, 12
L = (-0.55, 0.55, 0.63)


def put(x, y, ch, col):
    p.goto(x, y)
    p.pencolor(col)
    p.write(ch, font=FONT)


def planet(cx, cy, R, rgb, bands):
    for gy in range(-R, R + 1, CH):
        for gx in range(-R, R + 1, CW):
            d2 = gx * gx + gy * gy
            if d2 > R * R:
                continue
            nx, ny, nz = gx / R, gy / R, m.sqrt(R * R - d2) / R
            b = max(0.0, nx * L[0] + ny * L[1] + nz * L[2])
            if bands:
                b *= 0.8 + 0.2 * m.sin(gy * 0.18)
            ch = CHARS[min(9, int(b * 10))]
            if ch == " ":
                continue
            f = 0.45 + 0.55 * b
            put(cx + gx, cy + gy, ch, (int(rgb[0] * f), int(rgb[1] * f), int(rgb[2] * f)))
        s.update()


def ring(cx, cy, front):
    for k in range(160):
        a = 2 * m.pi * k / 160
        if (m.sin(a) < 0) != front:
            continue
        x = 235 * m.cos(a)
        y = 48 * m.sin(a)
        rx = x * m.cos(0.22) - y * m.sin(0.22)
        ry = x * m.sin(0.22) + y * m.cos(0.22)
        put(cx + rx, cy + ry, "=" if k % 3 else "-", (230, 190, 140))
    s.update()


for _ in range(70):
    put(random.uniform(-340, 330), random.uniform(-340, 330),
        random.choice([".", "+", "*", "."]), (200, 200, 255))

ring(-120, 70, False)
planet(-120, 70, 140, (255, 170, 90), True)
ring(-120, 70, True)
planet(190, -170, 95, (90, 160, 255), False)
t.done()
