# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


from copy import copy
from itertools import zip_longest
from typing import List


def get_data_from_file(path: str) -> str:
    with open(path, mode="r") as f:
        return f.read()


def main():
    personalised_letters: List[str] = []
    names: List[str] = get_data_from_file("Input/Names/invited_names.txt").split("\n")
    basic_letter = get_data_from_file("Input/Letters/starting_letter.txt")

    for name in names:
        personalised = copy(basic_letter).replace("[name]", name)
        personalised_letters.append(personalised)

    for name, letter in zip_longest(names, personalised_letters):
        with open(f"Output/ReadyToSend/Letter_for_{name}.txt", mode="a") as f:
            f.write(letter)


if __name__ == "__main__":
    main()
