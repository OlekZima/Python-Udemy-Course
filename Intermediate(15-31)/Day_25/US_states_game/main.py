import turtle
from typing import List
from numpy import isin
import pandas as pd



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
            break

        if answer_state in guessed_states:
            print(f"Guessed states: {guessed_states}")
            continue
        elif states_df["state"].isin([answer_state]).any():
            print(f"Guessed an {answer_state}")
            guessed_states.append(answer_state)
            if len(guessed_states) == len(states_df):
                break

    turtle.mainloop()


if __name__ == "__main__":
    main()
