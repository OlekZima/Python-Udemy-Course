from random import randint
from time import sleep
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Cross the Road")
    screen.tracer(0)
    screen.listen()

    player = Player()
    scoreboard = Scoreboard()
    car_manager = CarManager()

    level = 1
    game_speed_multipier = 0.7
    game_speed: float = 0.1

    game_is_on = True
    while game_is_on:
        screen.onkeypress(key="w", fun=player.move_up)
        scoreboard.write_level(f"Level {level}")
        if player.ycor() >= player.FINISH_LINE_Y:
            player.reset_pos()
            level += 1
            game_speed *= game_speed_multipier

        car_manager.move_cars(speed_multiplier=0)
        if randint(1, 7) == 2:
            car_manager.create_car(randint(-250, 250))
        car_manager.retrieve_cars()

        game_is_on = not player.is_car_collision(car_manager.get_cars())
        sleep(game_speed)
        screen.update()

    print("Game over!")


if __name__ == "__main__":
    main()
