# Gökkuşağı Spirali
import turtle

s = turtle.Screen()
s.setup(700, 700)
s.bgcolor("black")
s.tracer(0)
t = turtle.Turtle()
t.hideturtle()

colors = ["red", "orange", "yellow", "lime", "deepskyblue", "violet"]
for i in range(330):
    t.pencolor(colors[i % 6])
    t.width(i / 100 + 1)
    t.forward(i)
    t.left(59)
    if i % 5 == 0:
        s.update()

s.update()
turtle.done()
