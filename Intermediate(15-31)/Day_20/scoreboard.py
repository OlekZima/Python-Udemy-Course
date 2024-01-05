from turtle import Turtle
from typing import Tuple


class Scoreboard(Turtle):
    def __init__(self):
        self.FONT: Tuple[str, int, str] = ("Arial", 24, "bold")
        self.ALIGN: str = "center"

        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)
        self.score = 0

        self._write_score()

    def _write_score(self):
        self.clear()
        self.write(
            arg=f"Score: {self.score}",
            move=False,
            align=self.ALIGN,
            font=self.FONT,
        )

    def increment(self):
        self.score += 1
        self._write_score()
