from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
