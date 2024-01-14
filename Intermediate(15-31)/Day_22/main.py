import time
import turtle as t


def main():
    screen = t.Screen()
    screen.setup(600, 600)
    screen.tracer(0)

    is_game = True
    while is_game:
        screen.update()
        time.sleep(0.1)

    screen.exitonclick()


if __name__ == "__main__":
    main()
