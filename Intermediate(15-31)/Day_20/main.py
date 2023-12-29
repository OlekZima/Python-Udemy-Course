import time
import turtle as t
from typing import List


def init_turtle(i: int) -> t.Turtle:
    tmp_turtle = t.Turtle("square")
    tmp_turtle.shapesize(outline=0)
    tmp_turtle.penup()
    tmp_turtle.color("black", "white")
    tmp_turtle.goto(tmp_turtle.xcor() - i * 20, 0)
    return tmp_turtle


screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.title("Snake game")
screen.tracer(0)

segments = []
for i in range(3):
    segments.append(init_turtle(i))
screen.update()

while True:
    screen.update()
    time.sleep(0.1)
    for segment in segments:
        segment.forward(20)



screen.exitonclick()
