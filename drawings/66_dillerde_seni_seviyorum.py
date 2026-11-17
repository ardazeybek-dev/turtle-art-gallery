# Dillerde Seni Seviyorum
import turtle as t
import random

s = t.Screen()
s.setup(700, 700)
s.bgcolor("#0b0006")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.penup()

words = ["Seni seviyorum", "I love you", "Te amo", "Je t'aime", "Ich liebe dich",
         "Ti amo", "Eu te amo", "Aishiteru", "Saranghae", "Wo ai ni", "Kocham cie",
         "Ik hou van jou", "Jag alskar dig", "Te iubesc", "Volim te", "Szeretlek",
         "Mahal kita", "Seni sevirem", "愛してる", "사랑해", "我爱你"]
reds = ["#ff0a54", "#ff477e", "#ff7096", "#e5383b", "#ff8fab", "#c9184a", "#ffb3c6"]


def inside(x, y):
    u = x / 270
    v = (y + 30) / 270
    return (u * u + v * v - 1) ** 3 - u * u * v ** 3 <= 0


y = 300
while y > -310:
    x = -330
    while x < 330:
        word = random.choice(words)
        size = random.choice([9, 10, 11])
        w = len(word) * size * 0.75
        if inside(x, y) and inside(x + w, y) and inside(x + w / 2, y + 8):
            p.goto(x, y)
            p.pencolor(random.choice(reds))
            p.write(word, font=("Arial", size, "bold"))
            x += w + 8
        else:
            x += 8
    y -= 19
    s.update()

t.done()
