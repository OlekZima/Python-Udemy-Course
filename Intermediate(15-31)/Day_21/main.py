import turtle as t
from typing import List
from screen_turtle import ScreenTurtle
from paddle import Paddle
from ball import Ball
from time import sleep


def init_screen(width: int, height: int) -> t._Screen:
    screen = t.Screen()
    screen.setup(width, height)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)
    screen.listen()
    screen.update()
    return screen


def main(width: int, height: int):
    screen = init_screen(width, height)

    screen_turtle = ScreenTurtle(width, height)

    ball = Ball()

    l_paddle = Paddle(width)
    screen.onkeypress(key="w", fun=l_paddle.move_up)
    screen.onkeypress(key="s", fun=l_paddle.move_down)

    r_paddle = Paddle(width, is_player=False)
    screen.onkeypress(key="Up", fun=r_paddle.move_up)
    screen.onkeypress(key="Down", fun=r_paddle.move_down)

    paddles: list[Paddle] = [l_paddle, r_paddle]

    is_game = True
    while is_game:
        ball.move(paddles)
        sleep(0.1)

        # l_paddle miss
        if ball.xcor() < -380:
            ball.reset_ball()

        # r_paddle miss
        if ball.xcor() > 380:
            ball.reset_ball()

        screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    main(800, 600)
