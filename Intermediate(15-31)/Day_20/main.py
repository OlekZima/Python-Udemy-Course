import time
import turtle as t
from typing import List
from snake import Snake


screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()

is_game = True
while is_game:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
