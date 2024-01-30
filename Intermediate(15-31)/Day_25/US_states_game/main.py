import turtle
from typing import List, Tuple
from numpy import isin
import pandas as pd


def get_coords_by_name(dataframe: pd.DataFrame, state_name: str) -> Tuple[int, int]:
    x_cord: int = dataframe[dataframe["state"] == state_name]["x"].item()
    y_cord: int = dataframe[dataframe["state"] == state_name]["y"].item()
    return (x_cord, y_cord)


def main():
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "./blank_states_img.gif"
    states_df = pd.read_csv("./50_states.csv")
    screen.addshape(image)
    turtle.shape(image)
    state_writer = turtle.Turtle(visible=False)
    state_writer.penup()
    guessed_states: List[str] = []

    is_game: bool = True
    while is_game:
        answer_state = screen.textinput(
            f"{len(guessed_states)}/{len(states_df)} States Correct",
            "What's another state's name?",
        )
        if answer_state is not None:
            answer_state = answer_state.title()
        else:
            is_game = False

        if answer_state in guessed_states:
            print(f"Guessed states: {guessed_states}")
            continue
        elif states_df["state"].isin([answer_state]).any():
            print(f"Guessed an {answer_state}")
            try:
                guessed_states.append(answer_state)  # type: ignore
                state_writer.goto(get_coords_by_name(states_df, answer_state))  # type: ignore
            except TypeError:
                print("Cannot append `None` value to the `str` list.")
            except:
                print("Something is broken")
            state_writer.write(answer_state)
            if len(guessed_states) == len(states_df):
                is_game = False

    turtle.mainloop()


if __name__ == "__main__":
    main()
