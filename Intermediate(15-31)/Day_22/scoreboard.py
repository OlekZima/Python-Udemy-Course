from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.goto(-250, 250)

    def write_level(self, text: str):
        self.clear()
        self.write(text, font=FONT)
