import arts
from game_data import data
from random import randint, shuffle
from typing import List, Dict
from os import system

class Account():
    def __init__(self, dict_of_data: Dict[str, str]) -> None:
        self.name = dict_of_data["name"]
        self.follower_count = int(dict_of_data["follower_count"])
        self.description = dict_of_data["description"]
        self.country = dict_of_data["country"]
    
    def __str__(self) -> str:
        return f"{self.name}, a {self.description}, from {self.country}"

    def get_follower_count(self) -> int:
        return self.follower_count

def clear() -> None:
    system('cls')

def prepare_data() -> List[Account]:
    accounts = [Account(data_dict) for data_dict in data]
    shuffle(accounts)
    return accounts

def validate_user_input() -> str:
    is_validated = False
    while not is_validated:
        user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
        if user_input == 'A' or user_input == 'B':
            return user_input
        else:
            print("Invalid input!")
    return "Error"

def get_random_item_from_list(list: List[Account]) -> Account:
    return list.pop(randint(0, len(list) - 1))

def print_info(a: Account, b: Account, score: int = 0) -> None:
    print(arts.logo)
    if score != 0:
        print(f"You're right! Current score: {score}")

    print(f"Compare A: {a}")
    print(arts.vs)
    print(f"Against B: {b}")

def does_user_guessed(a: Account, b: Account, score: int = 0) -> bool:
    print_info(a, b, score)
    user_choice = validate_user_input()
    if user_choice == "Error":
        print("Error occured while validating input!")
        exit(1)
    
    if a.get_follower_count() > b.get_follower_count() and user_choice == 'A':
        return True
    
    if b.get_follower_count() > a.get_follower_count() and user_choice == 'B':
        return True

    return False

def reasign_accounts(account_1: Account, account_2: Account) -> Account:
    return account_1 if account_1.get_follower_count() > account_2.get_follower_count() else account_2

def game(accounts: List[Account]) -> None:
    score = 0
    account_a = get_random_item_from_list(accounts)
    account_b = get_random_item_from_list(accounts)
    is_game = True
    while is_game:
        round = does_user_guessed(account_a, account_b, score)
        if not round:
            is_game = False
        else:
            account_a = reasign_accounts(account_a, account_b)
            account_b = get_random_item_from_list(accounts)
            score += 1

        clear()

    print(arts.logo)
    print(f"Sorry, that's wrong. Final score: {score}")

    
if __name__ == '__main__':
    accounts = prepare_data()
    game(accounts)