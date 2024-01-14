from turtle import Turtle
from typing import List
from paddle import Paddle


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.speed("fastest")
        self.color("white")

        self.x_speed = 10
        self.y_speed = 10

        self.move_speed = 0.1

    def move(self, paddles: List[Paddle]):
        self.goto(self.xcor() + self.x_speed, self.ycor() + self.y_speed)
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()

        if (self.distance(paddles[0]) < 50 and self.xcor() < -320) or (
            self.distance(paddles[1]) < 50 and self.xcor() > 320
        ):
            self.bounce_x()

    def reset_ball(self):
        self.home()
        self.bounce_x()
        self.move_speed = 0.1

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1
        self.move_speed *= 0.9
