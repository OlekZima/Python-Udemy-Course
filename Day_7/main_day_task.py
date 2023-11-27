# Hangman game
from random import choice

def win():
    print("You win!")
    exit()

word_list = ["ardvark", "baboon", "camel"]

chosen_word = choice(word_list)
is_game_on = True
# Debug
print(f"Chosen word is {chosen_word}")

guessed_letters = ['_' for _ in range(len(chosen_word))]

while is_game_on:
    letter_input = input("Guess a letter: ").lower()

    if letter_input == chosen_word:
        win()

    for index, letter in enumerate(chosen_word):
        if letter == letter_input:
            guessed_letters[index] = letter

    [print(x, end=' ') for x in guessed_letters]
    print()
    
    if "".join(guessed_letters) == chosen_word:
        is_game_on = False

print("You win!")