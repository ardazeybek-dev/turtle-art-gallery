# Matrix Yağmuru
import turtle as t
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#000000")
s.colormode(255)
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.penup()

GLYPHS = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホ0123456789ABCDEF"
CW, CH = 14, 16

for col in range(50):
    x = -345 + col * CW
    for _ in range(random.randint(1, 2)):
        head = random.randint(0, 41)
        tail = random.randint(8, 26)
        for k in range(tail, -1, -1):
            row = head - k
            if row < 0:
                continue
            y = 330 - row * CH
            if k == 0:
                rgb = (220, 255, 220)
            else:
                f = 1 - k / (tail + 1)
                rgb = (0, int(60 + 195 * f), int(20 + 50 * f))
            p.goto(x, y)
            p.pencolor(rgb)
            p.write(random.choice(GLYPHS), font=("Courier", 11, "bold"))
    s.update()

t.done()
