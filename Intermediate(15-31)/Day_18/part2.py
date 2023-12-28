from random import random
from turtle import Turtle, Screen

def draw_a_figure(turtle: Turtle, number_of_vertices: int) -> None:
    if number_of_vertices < 2:
        raise ValueError
    angle: float = 360 / number_of_vertices
    for _ in range(number_of_vertices):
        turtle.forward(100)
        turtle.right(angle)

turtle = Turtle()
turtle.shape("turtle")
turtle.color("darkorange")

for i in range(3, 11):
    turtle.pencolor(random(), random(), random())
    draw_a_figure(turtle, i)



screen = Screen()
screen.exitonclick()
