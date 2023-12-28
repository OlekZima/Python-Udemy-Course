from random import randint
import turtle as t
from typing import Tuple

directions: dict[int, int] = {1: 0, 2: 90, 3: 180, 4: 270}


def pick_random_direction(turtle: t.Turtle):
    num: int = randint(1, 4)
    turtle.setheading(directions[num])


def random_color() -> Tuple[int, int, int]:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


jimmy = t.Turtle()
jimmy.shape("arrow")
jimmy.color("darkorange")
t.colormode(255)
jimmy.pensize(10)
jimmy.speed("fastest")

for _ in range(200):
    jimmy.pencolor(random_color())
    pick_random_direction(jimmy)
    jimmy.forward(20)


screen = t.Screen()
screen.exitonclick()
