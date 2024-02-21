import datetime as dt
from random import choice
import smtplib as smtp


def get_random_line_from_file(path: str) -> str:
    try:
        with open(path, "r") as f:
            content = f.read().split("\n")
            line = choice(content)
    except FileNotFoundError:
        print("File does not exist!")
        exit()
    else:
        return line


quote = get_random_line_from_file("./quotes.txt")
print(quote)
