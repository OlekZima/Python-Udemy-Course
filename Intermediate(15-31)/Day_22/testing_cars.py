from hmac import new
import time
from turtle import Screen
from typing import List
from car import Car
from random import choice, randint

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
COLORS: List[str] = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        self.cars: List[Car] = []

    def create_car(self, ycor: int):
        if len(self.cars) > 25:
            return
        new_car = Car()
        new_car.color(choice(COLORS))
        new_car.goto(new_car.xcor(), ycor)
        self.cars.append(new_car)

    def move_cars(self):
        move_distance = 5
        for car in self.cars:
            car.forward(move_distance)

    def get_cars(self) -> List[Car]:
        return self.cars

    def retrieve_cars(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.goto(300, randint(-250, 250))


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


car_manager = CarManager()

game_is_on = True
while game_is_on:
    car_manager.move_cars()

    if randint(1, 7) == 2:
        car_manager.create_car(randint(-250, 250))

    car_manager.retrieve_cars()
    time.sleep(0.1)
    screen.update()

print("GG")
