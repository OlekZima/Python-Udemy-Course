from typing import Dict
import pandas as pd


def main(alphabet_dict: Dict[str, str]):

    user_input = input("Enter a word: ").upper()

    try:
        result = [alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(result)


if __name__ == "__main__":
    alphabet_df: pd.DataFrame = pd.read_csv("./nato_phonetic_alphabet.csv")
    alphabet_dict: Dict[str, str] = {
        row["letter"]: row["code"] for (_, row) in alphabet_df.iterrows()
    }
    is_on = True
    while is_on:
        main(alphabet_dict)
