# Sakura Ağacı
import turtle as t
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#0a0a1f")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

pinks = ["#ffb7c5", "#ff9eb5", "#ffc8dd", "#ffe5ec", "#ff85a2"]


def blossom():
    for _ in range(3):
        p.dot(random.randint(6, 11), random.choice(pinks))
        p.penup()
        p.forward(random.uniform(3, 7))
        p.left(random.uniform(90, 150))


def branch(length, width):
    if length < 9:
        blossom()
        return
    p.width(width)
    p.pencolor("#3b2418" if width > 3 else "#5c3a2a")
    p.pendown()
    p.forward(length)
    sub = random.randint(2, 3)
    spread = random.uniform(40, 70)
    for k in range(sub):
        turn = -spread / 2 + spread * k / (sub - 1) + random.uniform(-8, 8)
        p.left(turn)
        branch(length * random.uniform(0.6, 0.75), width * 0.7)
        p.right(turn)
    p.penup()
    p.backward(length)
    s.update()


p.penup()
p.goto(-30, -310)
p.setheading(85)
branch(120, 16)

p.penup()
for _ in range(60):
    p.goto(random.uniform(-340, 340), random.uniform(-340, -150))
    p.dot(random.randint(4, 7), random.choice(pinks))
s.update()
t.done()
