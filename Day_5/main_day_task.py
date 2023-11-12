from random import randint, choice, sample
from string import ascii_letters

print("Welcome to the PyPassword Generator!")

pass_len = int(input("How many letters would you like in your password?\n"))
symbols_num = int(input("How many symbols would you like?\n"))
numbers_num = int(input("How many numbers would you like?\n"))

password = ""

for i in range(pass_len):
    password += choice(ascii_letters)

symbols = ['!', '#', '$', '%', '&', '()', ')', '*', '+']

for i in range(symbols_num):
    password += choice(symbols)

for i in range(numbers_num):
    password += str(randint(0, 9))

# password = "".join(sample(password, len(password)))
password = "".join(list(password))

print(f"Your password is {password}")