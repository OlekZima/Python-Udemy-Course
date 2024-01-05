import turtle as t
from typing import List, Dict
from enum import Enum


class Direction(Enum):
    Up = 90
    Down = 270
    Left = 180
    Right = 0


class Snake:
    def __init__(self, init_size: int = 3):
        self.MOVE_DISTANCE: int = 20
        self.segments: List[t.Turtle] = [Snake.init_turtle(i) for i in range(init_size)]
        self.head: t.Turtle = self.segments[0]
        self.head.color("Black")
        self.direction = self.head.heading()

    @staticmethod
    def init_turtle(offset_from_middle: int) -> t.Turtle:
        tmp_turtle = t.Turtle(shape="square")
        tmp_turtle.shapesize(outline=0)
        tmp_turtle.penup()
        tmp_turtle.color("black", "white")
        tmp_turtle.goto(tmp_turtle.xcor() - offset_from_middle * 20, 0)
        return tmp_turtle

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_pos: t.Vec2D = self.segments[segment_num - 1].position()
            self.segments[segment_num].goto(new_pos)
        self.head.forward(distance=self.MOVE_DISTANCE)

    def up(self) -> None:
        if self.direction == Direction.Down:
            return None

        self.head.setheading(to_angle=90)
        self.direction = Direction.Up

    def down(self) -> None:
        if self.direction == Direction.Up:
            return None

        self.head.setheading(to_angle=270)
        self.direction = Direction.Down

    def left(self) -> None:
        if self.direction == Direction.Right:
            return None

        self.head.setheading(to_angle=180)
        self.direction = Direction.Left

    def right(self) -> None:
        if self.direction == Direction.Left:
            return None

        self.head.setheading(to_angle=0)
        self.direction = Direction.Right
