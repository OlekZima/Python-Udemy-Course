import datetime as dt
from random import choice
import smtplib as smtp
import credentials


def get_random_line_from_file(path: str) -> str:
    try:
        with open(path, "r") as f:
            line = choice(f.read().split("\n"))
    except FileNotFoundError:
        print("File does not exist!")
        exit()
    else:
        return line


def main():
    day_of_week = dt.datetime.now().weekday()
    if day_of_week != 0:
        return
    quote = get_random_line_from_file("./quotes.txt")
    with smtp.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=credentials.gmail, password=credentials.gmail_app)
        connection.sendmail(
            credentials.gmail,
            to_addrs=credentials.mail_megumin,
            msg=f"Subject:New week - new qoute\n\n{quote}\n\nYour Olek Zima",
        )


if __name__ == "__main__":
    main()
