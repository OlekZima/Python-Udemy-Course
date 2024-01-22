from turtle import Turtle
from typing import List
from car import Car


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.FINISH_LINE_Y = 280
        self.MOVE_DISTANCE = 10
        self.speed("fastest")
        self.penup()
        self.setheading(90)
        self.STARTING_POSITION = (0, -280)
        self.goto(self.STARTING_POSITION)

    def move_up(self):
        self.forward(self.MOVE_DISTANCE)

    def reset_pos(self):
        self.goto(self.STARTING_POSITION)

    def is_car_collision(self, cars: List[Car]) -> bool:
        for car in cars:
            if self.distance(car) >= 30:
                continue
            return True
        else:
            return False
