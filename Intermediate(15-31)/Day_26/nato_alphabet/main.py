from typing import Dict, List
import pandas as pd


def main():
    alphabet_df: pd.DataFrame = pd.read_csv("./nato_phonetic_alphabet.csv")

    alphabet_dict: Dict[str, str] = {
        row["letter"]: row["code"] for (_, row) in alphabet_df.iterrows()
    }

    user_input = input("Enter a word: ").upper()

    result = [alphabet_dict.get(letter) for letter in user_input]

    print(result)


if __name__ == "__main__":
    main()
