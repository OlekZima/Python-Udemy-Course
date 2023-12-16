from typing import List, Tuple
from balckjack_logo import logo
from random import choice

def validate_yn_input(message_to_display: str) -> bool:
    """
    Validates user input for yes/no questions.

    Parameters:
        message_to_display (str): The message to display to the user.

    Returns:
        bool: True if the user input is 'y', 'yes', or 'yeah'. False if the user input is 'n', 'no', or 'nope'.
    """
    check_input_flag = True
    while check_input_flag:
        user_input = input(f"{message_to_display}").lower()
        if user_input in ['y', 'yes', 'yeah']:
            return True
        elif user_input in ['n', 'no', 'nope']:
            return False
        else:
            print("Input is not correct!")

def take_card_from_deck(deck: List[int]) -> int:
    """
    Takes a card from the deck and returns it.

    Parameters:
        deck (List[int]): A list representing the deck of cards.

    Returns:
        int: The card taken from the deck.
    """
    return choice(deck)

def is_player_won(players_sum: int, computers_sum: int) -> bool:
    """
    Checks if the player has won the game.

    Parameters:
        players_sum (int): The sum of the player's cards.
        computers_sum (int): The sum of the computer's cards.

    Returns:
        bool: True if the player has won, False otherwise.
    """
    return players_sum > computers_sum and players_sum <= 21

def pass_and_count(player_cards: List[int], computer_cards: List[int]) -> int:
    """
    Checks who is the winner by sum of the cards numbers.

    Parameters:
        player_cards (List[int]): Player's cards
        computer_cards (List[int]): Computer's cards
    
    Returns:
        int: `0` if it is a draw, `1` if player won and `2` if computers won
    """
    players_sum = sum(player_cards)
    computers_sum = sum(computer_cards)

    # Draw
    if players_sum == computers_sum:
        return 0

    # Player
    if players_sum == 21 and computers_sum != 21:
        return 1

    # Computer
    elif computers_sum == 21 and players_sum != 21:
        return 2

    # Player's sum is higher than pc's and less than or equal to 21
    if is_player_won(players_sum, computers_sum):
        return 1

    # Player's sum is greater than 21, but can be reduced by changing the value of Ace from 11 to 1
    if players_sum > 21 and 11 in player_cards:
        players_sum -= 10
        if is_player_won(players_sum, computers_sum):
            return 1

    # Computer's sum is higher than player's and less than or equal to 21
    if not is_player_won(players_sum, computers_sum):
        return 2

    # Computer's sum is greater than 21, but can be reduced by changing the value of Ace from 11 to 1
    if computers_sum > 21 and 11 in computer_cards:
        computers_sum -= 10
        if not is_player_won(players_sum, computers_sum):
            return 2

    # If none of the above conditions are met, it's a draw
    return 0

def endgame(player_cards: List[int], computer_cards: List[int], message: str) -> None:
    """
    Prints the endgame message along with the computer's and player's cards and their sums.

    Parameters:
        player_cards (List[int]): The list of player's cards.
        computer_cards (List[int]): The list of computer's cards.
        message (str): The endgame message to be displayed.

    Returns:
        None
    """
    print(f"\t{message}")
    print(f"\tComputer's card: {computer_cards}. Sum is {sum(computer_cards)}")
    print(f"\tYour cards are {player_cards}. Sum is {sum(player_cards)}")

def check_winner(number: int, player_cards: List[int], computer_cards: List[int]) -> None:
    """
    Determines the winner of the blackjack game based on the given number.

    Parameters:
        number (int): The result of the blackjack game. 2 represents the computer winning, 1 represents the player winning, 0 represents a draw, and any other number represents an unhandled case.
        player_cards (List[int]): The cards of the player.
        computer_cards (List[int]): The cards of the computer.

    Returns:
        None
    """
    if number == 2: # PC won
        endgame(player_cards, computer_cards, "Computer is the winner!")
    elif number == 1: # Player won
        endgame(player_cards, computer_cards, "You are the winner!")
    elif number == 0:
        endgame(player_cards, computer_cards, "Draw!")
    else:
        endgame(player_cards, computer_cards, "Hasn't been handled yet!")

def init_game(deck: List[int]) -> Tuple[List[int], List[int]]:
    """
    Initializes a new game of blackjack.

    Parameters:
        deck (List[int]): A list representing the deck of cards.

    Returns:
        Tuple[List[int], List[int]]: A tuple containing the player's cards and the computer's cards.
    """
    player_cards = [take_card_from_deck(deck) for _ in range(2)]
    computer_cards = [take_card_from_deck(deck) for _ in range(2)]
    return (player_cards, computer_cards)

def blackjack(deck: List[int], player_cards: List[int], computer_cards: List[int]):
    """
    Simulates a game of blackjack.

    Args:
        deck (List[int]): The deck of cards.
        player_cards (List[int]): The cards in the player's hand.
        computer_cards (List[int]): The cards in the computer's hand.
    """
    print(logo)
    next_card = True
    while next_card:
        print(f"Your cards: {player_cards}. Sum is {sum(player_cards)}")
        print(f"Computer's first card: {computer_cards[0]}.")
        is_next_card = validate_yn_input("Type 'y' to get another card, type 'n' to pass: ")
        if not is_next_card:
            winners_code = pass_and_count(player_cards, computer_cards)
            check_winner(winners_code, player_cards, computer_cards)
            return
        else:
            player_cards.append(take_card_from_deck(deck))
            if sum(player_cards) > 21:
                endgame(player_cards, computer_cards, "Computer is the winner!")
                return

def game() -> None:
    """
    Function to play a game of Blackjack.

    The function prompts the user if they want to play a game of Blackjack.
    If the user chooses to play, it initializes the deck, starts the game,
    and asks if the user wants to play another game after each round.
    If the user chooses not to play, it prints "Bye!" and exits the function.

    Parameters:
        None

    Returns:
        None
    """
    if validate_yn_input("Do you want to play a game of Blackjack? Type 'y' or 'n': "):
        deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        another_game = True
        while another_game:
            player, computer = init_game(deck)
            blackjack(deck, player, computer)
            another_game = validate_yn_input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
    else:
        print("Bye!")

if __name__ == "__main__":
    game
