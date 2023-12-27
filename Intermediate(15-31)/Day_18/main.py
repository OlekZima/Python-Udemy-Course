from turtle import Turtle, Screen

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

screen = Screen()
screen.exitonclick()
