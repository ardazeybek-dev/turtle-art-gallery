# Kar Kristali
import turtle as t

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#010915")
s.tracer(0)
p = t.Turtle()
p.hideturtle()

colors = {3: "#ffffff", 2: "#bde0fe", 1: "#7cc6fe", 0: "#4ea8de"}


def branch(length, depth):
    p.pencolor(colors[depth])
    p.width(depth + 1)
    if depth == 0:
        p.forward(length)
        p.backward(length)
        return
    for _ in range(3):
        p.forward(length / 3)
        p.left(55)
        branch(length * 0.36, depth - 1)
        p.right(110)
        branch(length * 0.36, depth - 1)
        p.left(55)
        p.pencolor(colors[depth])
        p.width(depth + 1)
    p.backward(length)


for k in range(6):
    p.setheading(90 + k * 60)
    branch(240, 3)
    s.update()

p.pencolor("white")
p.width(2)
p.penup()
p.goto(0, -40)
p.setheading(0)
p.pendown()
p.circle(40, steps=6)
s.update()
t.done()
