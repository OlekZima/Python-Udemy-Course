from typing import List
from car import Car
from random import choice, randint


class CarManager:
    def __init__(self):
        self.cars: List[Car] = []
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10
        self.COLORS: List[str] = ["red", "orange", "yellow", "green", "blue", "purple"]

    def create_car(self, ycor: int):
        if len(self.cars) > 25:
            return
        new_car = Car()
        new_car.color(choice(self.COLORS))
        new_car.goto(new_car.xcor(), ycor)
        self.cars.append(new_car)

    def move_cars(self, speed_multiplier: int):
        move_distance = 5
        for car in self.cars:
            car.forward(move_distance + self.MOVE_INCREMENT * speed_multiplier)

    def get_cars(self) -> List[Car]:
        return self.cars

    def retrieve_cars(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.goto(300, randint(-250, 250))
