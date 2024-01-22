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

    """
    Came with idea for 2 possible implementations for speed/difficulty increasing.
    First one:
        Some multiplier that decreases wait time in sleep fun (end of the file)
    
    Second one:
        Just increase delta_x for moving cars, but at the highest Levels cars would just teleport like
        half a screen
    """
    game_speed_multipier = 0.7
    game_speed: float = 0.1

    game_is_on = True
    while game_is_on:
        screen.onkeypress(key="w", fun=player.move_up)
        if player.ycor() >= player.FINISH_LINE_Y:
            player.reset_pos()
            scoreboard.increase_level_update_scoreboard()
            game_speed *= game_speed_multipier

        car_manager.move_cars(
            speed_multiplier=0
        )  # for the second option must be the level from `scoreboard.get_level()`
        if randint(1, 7) == 2:
            car_manager.create_car(randint(-250, 250))
        car_manager.retrieve_cars()

        game_is_on = not player.is_car_collision(car_manager.get_cars())
        sleep(game_speed)  # for the second option must be const 0.1
        screen.update()

    print("Game over!")


if __name__ == "__main__":
    main()
