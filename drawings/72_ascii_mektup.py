# ASCII Mektup
import turtle as t
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#120610")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.penup()

CW, CH = 8, 14
FONT = ("Courier", 10, "bold")
W, H = 270, 170


def put(x, y, ch, col):
    p.goto(x, y)
    p.pencolor(col)
    p.write(ch, font=FONT)


def in_heart(x, y):
    u = x / 55
    v = (y + 25) / 55
    return (u * u + v * v - 1) ** 3 - u * u * v ** 3 <= 0


for y in range(H, -H - 1, -CH):
    for x in range(-W, W + 1, CW):
        top = H + (-abs(x)) * (H + 10) / W
        bottom = -H + (W - abs(x)) * 0.7
        if abs(x) >= W - CW or abs(y) >= H - CH // 2:
            ch, col = "#", "#f4a261"
        elif in_heart(x, y):
            ch, col = "@", random.choice(["#ff0a54", "#e5383b", "#ff477e"])
        elif abs(y - top) < CH * 0.6:
            ch, col = ("\\" if x < 0 else "/"), "#ffffff"
        elif abs(y - bottom) < CH * 0.6:
            ch, col = ("/" if x < 0 else "\\"), "#ffe8d6"
        else:
            ch, col = random.choice([".", ":", "."]), random.choice(["#e9c46a", "#d4a373"])
        put(x, y, ch, col)
    s.update()

for _ in range(26):
    put(random.uniform(-300, 300), random.uniform(200, 330), "♥",
        random.choice(["#ff4d88", "#ff99bb", "#ffccd5"]))
s.update()
t.done()
