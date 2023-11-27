# Hangman game
from random import choice
from hangman_art import logo, stages
from hangman_words import word_list
def win():
    print("You win!")
    exit()

def lose():
    print("You lose!")
    exit()

def print_under_lines():
    [print(x, end=' ') for x in guessed_letters]
    print()

chosen_word = choice(word_list)
remaining_lives = len(stages) - 1

# Debug
# print(f"Chosen word is {chosen_word}")

print(logo)

guessed_letters = ['_' for _ in range(len(chosen_word))]

is_game_on = True
while is_game_on:
    if (remaining_lives <= 0):
        lose()

    letter_input = input("Guess a letter: ").lower()

    if letter_input == chosen_word:
        win()
    
    if letter_input not in chosen_word:
        print(f"There is no such letter!")
        remaining_lives -= 1
    elif letter_input in guessed_letters:
        print(f"You have already guessed letter {letter_input}!")

    for index, letter in enumerate(chosen_word):
        if letter == letter_input:
            guessed_letters[index] = letter

    if "".join(guessed_letters) == chosen_word:
        win()    
    print_under_lines()
    print(stages[remaining_lives])
