import turtle as t
from screen_turtle import ScreenTurtle
from paddle import Paddle


def init_screen(width: int, height: int):
    screen = t.Screen()
    screen.setup(width, height)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)
    screen.listen()
    screen.update()
    return screen


width = 800
height = 600
screen = init_screen(800, 600)

screen_turtle = ScreenTurtle(width, height)


player = Paddle()
screen.onkeypress(key="w", fun=player.move_up)
screen.onkeypress(key="s", fun=player.move_down)

enemy = Paddle()
screen.onkeypress(key="Up", fun=enemy.move_up)
screen.onkeypress(key="Down", fun=enemy.move_down)


while True:
    screen.update()

screen.exitonclick()
