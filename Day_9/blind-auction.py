from blind_auction_logo import logo
from os import system

def clear() -> None:
    system('cls')

def new_bidder(bidders_dict: dict(str, int)) -> None:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders_dict[name] = bid

def find_winner(bidders_dict: dict(str, int)) -> str:
    v = list(bidders_dict.values())
    k = list(bidders_dict.keys())
    return k[v.index(max(v))]

def main_game() -> None:
    bidders = {}

    print(logo)
    print("Welcome to the secret auction program.")
    is_auction = True
    while is_auction:
        new_bidder(bidders)
        other_bidders = input("are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if other_bidders == "no":
            break
        clear()

    winner = find_winner(bidders)
    print(f"The winner is {winner} with a bid of ${bidders[winner]}.")

if __name__ == "__main__":
    main_game()