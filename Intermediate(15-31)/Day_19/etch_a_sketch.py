import turtle as t


def forward():
    jimmy.forward(10)


def backward():
    jimmy.backward(10)


def left():
    jimmy.left(10)


def right():
    jimmy.right(10)


def reset():
    jimmy.home()
    jimmy.clear()


if __name__ == "__main__":
    jimmy = t.Turtle()
    screen = t.Screen()

    screen.listen()
    screen.onkeypress(fun=forward, key="w")
    screen.onkeypress(fun=backward, key="s")
    screen.onkeypress(fun=left, key="a")
    screen.onkeypress(fun=right, key="d")
    screen.onkey(fun=reset, key="c")

    screen.exitonclick()
