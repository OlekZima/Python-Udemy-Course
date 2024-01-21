from typing import List
from car import Car

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
COLORS: List[str] = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        self.cars: List[Car] = []

    def create_car(self):
        new_car = Car()
        self.cars.append(new_car)

    def move_cars(self):
        move_distance = 5
        for car in self.cars:
            car.forward(move_distance)

    def get_cars(self) -> List[Car]:
        return self.cars
