print("Welcome to the treasure island.\nYour mission is to find the treasure.")
choise_one = input("Choose where do you go? Left or right?\n").lower()

if choise_one != "left":
    print("Game over!")
    exit()

choise_two = input("You make it to the river.\nDo you want to wait to the boat or swim by your own?\n").lower()

if choise_two != "wait":
    print("Game over!")
    exit()

choise_three = input("You see 3 doors in front of you. Red, Green and Blue.\nYou have to choise one.\n").lower()

if choise_three != "green":
    print("Game over!")
    exit()

print("You win! You found the treasure!")