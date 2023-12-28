from turtle import Turtle, Screen

def draw_a_figure(turtle: Turtle, number_of_vertices: int) -> None:
    angle: int = int(360 / number_of_vertices)
    for _ in range(angle):
        turtle.forward(100)
        turtle.right(angle)

turtle = Turtle()
turtle.shape("turtle")
turtle.color("darkorange")

for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.left(90)

for _ in range(15):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()


draw_a_figure(turtle, 3)

screen = Screen()
screen.exitonclick()
