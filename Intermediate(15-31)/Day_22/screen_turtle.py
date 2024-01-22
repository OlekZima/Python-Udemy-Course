from turtle import Turtle


class ScreenTurtle(Turtle):
    def __init__(self, height: int = 600):
        super().__init__(visible=False)
        self.speed("fastest")
        self.penup()
        self.pensize(width=4)
        self.goto(x=0, y=height / 2)
        self.pencolor("white")
        self.setheading(270)
        self.create_line()

    def create_line(self):
        for _ in range(20):
            self.forward(15)
            self.pendown()
            self.forward(15)
            self.penup()
