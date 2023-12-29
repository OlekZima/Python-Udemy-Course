import turtle as t
from typing import List


def create_turtles() -> List[t.Turtle]:
    return [t.Turtle() for _ in range(5)]
