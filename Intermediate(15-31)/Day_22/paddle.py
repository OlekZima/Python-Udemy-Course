from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, screen_width: int, is_player: bool = True):
        super().__init__(shape="square")
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_wid=1, stretch_len=5)

        if not is_player:
            self.goto(screen_width / 2 - 40, 0)
        else:
            self.goto(-screen_width / 2 + 40, 0)
        self.setheading(90)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
