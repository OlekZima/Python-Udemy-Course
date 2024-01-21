from turtle import Turtle, distance
from typing import List
from car import Car

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.speed("fastest")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_pos(self):
        self.goto(STARTING_POSITION)

    def is_car_collision(self, cars: List[Car]) -> bool:
        for car in cars:
            if self.distance(car) >= 30:
                continue
            return True
        else:
            return False
