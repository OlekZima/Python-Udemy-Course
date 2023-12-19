from gues_a_number_logo import logo
from random import randint

def greet_and_get_difficulty() -> bool:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    input_validated = False
    while not input_validated:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty in ["easy", "e"]:
            return True
        elif difficulty in ["hard", "h"]:
            return False
        else:
            print("Incorrect input!")

def validate_int_input() -> int:
    validated = False
    while not validated:
        try:
            number = int(input("\nMake a guess: "))
            validated = True
        except ValueError:
            print("Your input is not a number!")
    return number

def check_guess(remaining_attempts: int, number_to_guess: int) -> bool:
    print(f"You have {remaining_attempts} attempts remainig to guess the number.")
    guess = validate_int_input()
    if guess < number_to_guess:
        print(f"{guess} is too low. Try again.")
        return False
    elif guess > number_to_guess:
        print(f"{guess} is too high. Try again.")
        return False
    else:
        print("Exactly!")
        return True

def game() -> None:
    number_to_guess = randint(1, 100)
    is_easy = greet_and_get_difficulty()
    print(f"pssssssssst, it's {number_to_guess}")
    lives = 10 if is_easy else 5

    while lives > 0:
        is_guessed = check_guess(lives, number_to_guess)
        if not is_guessed:
            lives -= 1
        else:
            break
    else:
        print("You lost.")
        return

    print(f"You won with {lives} remaining lives!")


if __name__ == "__main__":
    game()