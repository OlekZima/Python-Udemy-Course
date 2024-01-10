import turtle as t
from screen_turtle import ScreenTurtle
from paddle import Paddle
from ball import Ball


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

    player = Paddle(width)
    screen.onkeypress(key="w", fun=player.move_up)
    screen.onkeypress(key="s", fun=player.move_down)

    computer = Paddle(width, is_player=False)
    screen.onkeypress(key="Up", fun=computer.move_up)
    screen.onkeypress(key="Down", fun=computer.move_down)

    # ball_tick_speed =
    target_x, target_y = width / 2 - 20, height / 2 - 20
    slope = (target_y - ball.ycor()) / (target_x - ball.xcor())
    x_step = 0.5

    is_game = True
    while is_game:
        ball_x, ball_y = ball.pos()
        if ball_x < target_x and ball_y < target_y:
            ball.goto(ball.xcor() + x_step, ball.ycor() + x_step * slope)

        screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    width = 800
    height = 600
    main(800, 600)
