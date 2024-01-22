from turtle import Turtle
from typing import Tuple


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.level: int = 1
        self.penup()
        self.goto(-250, 250)
        self.FONT: Tuple[str, int, str] = ("Courier", 24, "normal")

    def write_level(self, text: str):
        self.clear()
        self.write(text, font=self.FONT)

    def increase_level_update_scoreboard(self):
        self.level += 1
        self.write_level(f"Level {self.level}")

    def get_level(self) -> int:
        return self.level
