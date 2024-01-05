import turtle as t
from typing import List


class Snake:
    def __init__(self, init_size: int = 3):
        self.segments: List[t.Turtle] = [Snake.init_turtle(i) for i in range(init_size )]

    @staticmethod
    def init_turtle(i: int) -> t.Turtle:
        tmp_turtle = t.Turtle("square")
        tmp_turtle.shapesize(outline=0)
        tmp_turtle.penup()
        tmp_turtle.color("black", "white")
        tmp_turtle.goto(tmp_turtle.xcor() - i * 20, 0)
        return tmp_turtle

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[segment_num - 1].position()
            self.segments[segment_num].goto(new_pos)
        self.segments[0].forward(20)
