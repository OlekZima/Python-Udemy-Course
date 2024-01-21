import time
from turtle import Screen
from player import FINISH_LINE_Y, Player
from car_manager import CarManager
from scoreboard import Scoreboard
from car import Car

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

car_manager.create_car()

game_is_on = True
while game_is_on:
    screen.onkeypress(key="w", fun=player.move_up)
    if player.ycor() >= FINISH_LINE_Y:
        player.reset_pos()
    car_manager.move_cars()

    game_is_on = not player.is_car_collision(car_manager.get_cars())

    time.sleep(0.1)
    screen.update()

print("GG")
