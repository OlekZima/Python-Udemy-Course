from random import randint

ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

ARTS = [ROCK, PAPER, SCISSORS]

player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

print(ARTS[player_choose])

computer_choose = randint(0, 2)
print("Computer chose:")
print(ARTS[computer_choose])

if player_choose == 0 and computer_choose == 1:
    print("You lose") # P: ROCK C: PAPER
elif player_choose == 1 and computer_choose == 2:
    print("You lose") # P: PAPER C: SCISSORS
elif player_choose == 2 and computer_choose == 0:
    print("You lose") # P: SCISSORS C: ROCK
elif player_choose == 2 and computer_choose == 1:
    print("You win")  # P: SCISSORS C: PAPER
elif player_choose == 0 and computer_choose == 2:
    print("You win")  # P: ROCK C: SCISSORS
elif player_choose == 1 and computer_choose == 0:
    print("You win")  # P: PAPER C: ROCK
else:
    print("Tie")


