# Altın Spiral
import turtle as t

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#0a0700")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
scale = 2.3

p.penup()
p.goto(73, 118)
p.setheading(0)
p.pendown()
for f in fib:
    side = f * scale
    p.pencolor("#6b5520")
    p.width(1.5)
    for _ in range(4):
        p.forward(side)
        p.left(90)
    p.pencolor("#ffd166")
    p.width(3)
    p.circle(side, 90)
    s.update()

t.done()
