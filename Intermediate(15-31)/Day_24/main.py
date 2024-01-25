import time
import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

is_game: bool = True
while is_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Check food collision
    if snake.head.distance(x=food) <= 15:
        # print("am")
        scoreboard.increment()
        food.refresh()
        snake.extend()
        # snake.segments.append(snake.init_turtle(len(snake.segments)))

    is_stopped: bool = snake.is_wall_collision() or snake.is_tail_collision()
    if is_stopped:
        scoreboard.reset()
        snake.reset()

# scoreboard.game_over()
screen.exitonclick()
