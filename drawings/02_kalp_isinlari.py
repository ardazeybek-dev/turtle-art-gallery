# Kalp Işınları
import turtle
import math

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.tracer(0)
t = turtle.Turtle()
t.hideturtle()
t.pensize(1)

colors = ["#ff3366", "#ff9933", "#ffee33", "#33ff99",
          "#33ccff", "#9966ff", "#ff66cc"]

for i in range(150):
    angle = i * (math.pi * 2) / 150
    x = 16 * math.sin(angle) ** 3 * 17
    y = (13 * math.cos(angle) - 5 * math.cos(2 * angle)
         - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * 17 + 40
    c = colors[i % len(colors)]
    t.color(c)
    t.penup()
    t.goto(0, -20)
    t.pendown()
    t.goto(x, y)
    for _ in range(8):
        t.forward(7)
        t.backward(7)
        t.right(45)
    screen.update()

turtle.done()
