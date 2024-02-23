from typing import Dict, List
import pandas as pd
from random import choice
import datetime
import smtplib
import os
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv


def get_data(path: str) -> pd.DataFrame:
    try:
        data_df = pd.read_csv(path)
    except FileNotFoundError:
        print("CSV file does not exists")
    return data_df


def get_people(data_df: pd.DataFrame) -> Dict:
    datetime_now = datetime.datetime.now()
    month_now = datetime_now.month
    day_now = datetime_now.day

    tmp_df = data_df[data_df["month"] == month_now]
    people_to_wish_df = tmp_df[tmp_df["day"] == day_now]

    people_dict = people_to_wish_df.to_dict(orient="split", index=False)
    return people_dict


def get_random_letter(path_to_letters: str) -> str:
    files = os.listdir(path_to_letters)
    chosen_file = choice(files)
    with open(f"./{path_to_letters}/{chosen_file}", "r") as file:
        file_data = file.read()

    return file_data


def send_letter(smtp_host: str, user_mail: str, app_password: str,
                from_mail: str, to_mail: str, letter: str):
    with smtplib.SMTP(smtp_host) as connection:
        connection.starttls()
        connection.login(user_mail, app_password)
        connection.sendmail(from_mail, to_mail,
                            f"Subject:Happy Birthday!\n\n{letter}")


def main():
    data_df = get_data("./birthdays.csv")
    people_dict = get_people(data_df)
    if not people_dict["data"]:
        return

    for data in people_dict["data"]:
        name = data[0]
        mail = data[1]
        filled_letter = get_random_letter(
            "./letter_templates/").replace("[NAME]", name)
        
        # TODO: place send_letter() fun with filled data. 
        # Create dotenv and figure out how to work with it
        print(filled_letter)
        print("=" * 80)


if __name__ == "__main__":
    main()


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
