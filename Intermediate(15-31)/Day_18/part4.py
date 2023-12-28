from random import randint
import turtle as t
from typing import Tuple


def random_color() -> Tuple[int, int, int]:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def draw_spirograph(jimmy: t.Turtle, how_many_circles: int):
    angle = 360 / how_many_circles
    for _ in range(how_many_circles):
        jimmy.circle(100)
        jimmy.color(random_color())
        jimmy.left(angle)


jimmy = t.Turtle()
jimmy.shape("arrow")
jimmy.color("darkorange")
t.colormode(255)
jimmy.speed("fastest")

draw_spirograph(jimmy, 25)


screen = t.Screen()
screen.exitonclick()
