from random import randint
import turtle as t
from typing import List


class Race:
    def __init__(self, colors: List[str]):
        self._screen = t.Screen()
        self._screen.setup(width=500, height=400)

        t.colormode(255)
        self._colors = colors
        self._turtles = [t.Turtle("turtle") for _ in range(len(colors))]
        for i, turtle in enumerate(self._turtles):
            turtle.color(colors[i])

        self._move_turtles_to_start()

    def get_turtles(self) -> List[t.Turtle]:
        return self._turtles

    def get_screen(self):
        return self._screen

    def _move_turtles_to_start(self, dy: int = 25):
        i = 0
        for turtle in self._turtles:
            turtle.penup()
            turtle.goto(x=-230, y=-125 + i)
            i += dy

    @staticmethod
    def _go_for_random(turtle: t.Turtle):
        turtle.forward(randint(5, 10))

    def validate_str_input(self, title: str, prompt: str) -> str:
        is_validated = False
        users_input = ""
        while not is_validated:
            tmp = self._screen.textinput(
                title=title,
                prompt=prompt,
            )
            if tmp is None:
                break
            users_input = str(tmp).lower()

            if users_input not in self._colors:
                continue
            is_validated = True
        return users_input

    def race(self) -> t.Turtle:
        is_race: bool = True
        winner = self._turtles[0]
        while is_race:
            for turtle in self._turtles:
                self._go_for_random(turtle)
                x, y = turtle.pos()

                if x < 230:
                    continue
                winner = turtle
                return winner
        return winner


def main():
    colors: list[str] = ["purple", "blue", "green", "yellow3", "orange", "red"]
    race = Race(colors)
    screen = race.get_screen()

    users_turtle_color = race.validate_str_input(
        title="Make Your bet!",
        prompt="Which turtle is going to win this race? Enter a color: ",
    )
    winner = race.race()
    winners_color = winner.color()[0]

    if users_turtle_color == winners_color:
        print("Your turtle is winner!")
    elif users_turtle_color == "":
        print(f"{winners_color} is the winner!")
    else:
        print(f"Looser! {winners_color} turtle won this!")

    screen.exitonclick()


if __name__ == "__main__":
    main()
