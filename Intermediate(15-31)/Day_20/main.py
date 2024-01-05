import time
import turtle as t
from snake import Snake


screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.title("Snake game")
screen.tracer(0)

snake = Snake(init_size=3)

screen.listen()
screen.onkeypress(key="Up", fun=snake.up)
screen.onkeypress(key="Down", fun=snake.down)
screen.onkeypress(key="Left", fun=snake.left)
screen.onkeypress(key="Right", fun=snake.right)

is_game = True
while is_game:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
