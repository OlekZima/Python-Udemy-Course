import turtle as t


class ScreenTurtle(t.Turtle):
    def __init__(self, screen: t._Screen, width: int = 800, height: int = 600):
        screen.setup(width=width, height=height)
        screen.bgcolor("black")
        screen.title("Pong")
        self = t.Turtle(visible=False)
        self.penup()
        self.pensize(width=4)
        self.goto(x=0, y=height / 2)
        self.pencolor("white")
        self.setheading(270)
        for _ in range(20):
            self.forward(15)
            self.pendown()
            self.forward(15)
            self.penup()
