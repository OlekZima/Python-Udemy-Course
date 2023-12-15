from balckjack_logo import logo

def does_game_starts() -> bool:
    check_input_flag = True
    while check_input_flag:
        user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no', 'nope']:
            return False
        else:
            print("Input is not correct!")

def blackjack():
    print(logo)

if __name__ == "__main__":
    if does_game_starts():
        blackjack()
    else:
        print("Bye!")