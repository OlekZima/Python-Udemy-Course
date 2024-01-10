from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.speed("fastest")
        self.color("white")

    def move_to_the_point(self, x: int, y: int, speed: float = 0.5):
        # x -= 20
        # y -= 20
        slope = 0
        try:
            slope: float = (y - self.ycor()) / (x - self.xcor())
        except ZeroDivisionError:
            print("lol, zero division")

        x_step: float = speed

        print(slope)

        while self.xcor() < x and self.ycor() < y:
            self.goto(self.xcor() + x_step, self.ycor() + x_step * slope)
