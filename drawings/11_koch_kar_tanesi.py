# Koch Kar Tanesi
import turtle as t

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#020814")
s.tracer(0)
p = t.Turtle()
p.hideturtle()


def koch(length, depth):
    if depth == 0:
        p.forward(length)
        return
    length /= 3
    koch(length, depth - 1)
    p.left(60)
    koch(length, depth - 1)
    p.right(120)
    koch(length, depth - 1)
    p.left(60)
    koch(length, depth - 1)


def snowflake(size, depth, color, x, y):
    p.penup()
    p.goto(x, y)
    p.setheading(0)
    p.pendown()
    p.pencolor(color)
    p.width(2)
    for _ in range(3):
        koch(size, depth)
        p.right(120)
        s.update()


snowflake(460, 4, "#3fd0ff", -230, 133)
snowflake(300, 3, "#b48cff", -150, 87)
snowflake(150, 2, "white", -75, 43)
t.done()
