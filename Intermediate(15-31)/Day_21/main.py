import turtle as t
from screen_turtle import ScreenTurtle
from paddle import Paddle


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

    player = Paddle(width)
    screen.onkeypress(key="w", fun=player.move_up)
    screen.onkeypress(key="s", fun=player.move_down)

    computer = Paddle(width, is_player=False)
    screen.onkeypress(key="Up", fun=computer.move_up)
    screen.onkeypress(key="Down", fun=computer.move_down)

    while True:
        screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    width = 800
    height = 600
    main(800, 600)
