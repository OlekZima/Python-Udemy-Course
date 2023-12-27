from random import randint

names = input().split(", ")

if len(names) < 1:
    print("Enter at least one name!")
    exit()

chosen_person = randint(0, len(names) - 1)
print(f"{names[chosen_person]} is going to buy the meal!")