from turtle import Turtle, Screen

# Creating object example
timmy = Turtle()
print(timmy)

# Methods example
timmy.shape("turtle")
timmy.color("red", "green")
timmy.fd(100)

my_screen = Screen()

# Attribute example
print(my_screen.canvwidth)

my_screen.exitonclick()
