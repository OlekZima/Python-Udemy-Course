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

        self.high_score = 0
        self._write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0

        self._write_prompt(f"Score: {self.score} High Score: {self.high_score}")

    def _write_score(self):
        self._write_prompt(f"Score: {self.score} High Score: {self.high_score}")

    def _write_prompt(self, prompt: str, is_clear: bool = True):
        if is_clear:
            self.clear()

        self.write(
            arg=prompt,
            move=False,
            align=self.ALIGN,
            font=self.FONT,
        )

    def increment(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score

        self._write_prompt(f"Score: {self.score} High Score: {self.high_score}")
