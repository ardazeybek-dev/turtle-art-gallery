# Sonbahar Ağacı
import turtle as t
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#0b0603")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

leaves = ["#ff7b00", "#ffb700", "#e63946", "#f4a261", "#ffd60a"]


def branch(length, depth):
    if depth == 0:
        p.dot(random.randint(5, 9), random.choice(leaves))
        return
    p.width(depth * 1.1)
    p.pencolor("#8a5a3c" if depth > 4 else "#c98b6b")
    p.pendown()
    p.forward(length)
    a = random.uniform(18, 30)
    p.left(a)
    branch(length * random.uniform(0.68, 0.76), depth - 1)
    p.right(2 * a)
    branch(length * random.uniform(0.68, 0.76), depth - 1)
    p.left(a)
    p.penup()
    p.backward(length)
    s.update()


p.penup()
p.goto(0, -320)
p.setheading(90)
branch(125, 10)
s.update()
t.done()
