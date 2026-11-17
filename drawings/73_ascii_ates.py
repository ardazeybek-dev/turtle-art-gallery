# ASCII Ateş
import turtle as t
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#000000")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.penup()

COLS, ROWS = 84, 45
CW, CH = 8, 14
MAXH = 36
CHARS = " .,-~:;=!*#$@"
PALETTE = ["#1f0700", "#3d0c02", "#6a040f", "#9d0208", "#d00000", "#dc2f02",
           "#e85d04", "#f48c06", "#faa307", "#ffba08", "#ffd166", "#fff3b0"]

heat = [[0] * COLS for _ in range(ROWS)]
for x in range(COLS):
    d = abs(x - COLS / 2) / (COLS * 0.3)
    heat[0][x] = int(MAXH * max(0, 1 - d * d))

for y in range(1, ROWS):
    for x in range(COLS):
        src = min(COLS - 1, max(0, x + random.randint(-1, 1)))
        decay = 1 if random.random() < 0.45 + 0.9 * y / ROWS else 0
        heat[y][x] = max(0, heat[y - 1][src] - decay - (random.random() < 0.08) * 3)

for y in range(ROWS):
    for x in range(COLS):
        h = heat[y][x]
        if h == 0:
            continue
        f = h / MAXH
        p.goto(-336 + x * CW, -330 + y * CH)
        p.pencolor(PALETTE[min(11, int(f * 12))])
        p.write(CHARS[min(12, int(f * 13))], font=("Courier", 10, "bold"))
    s.update()

t.done()
