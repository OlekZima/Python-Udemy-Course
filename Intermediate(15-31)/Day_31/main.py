import tkinter as tk
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"


def get_csv_data(path: str):
    with open(path, "r"):
        data = pd.read_csv(path)
        data_dict = {row["French"]: row["English"] for (_, row) in data.iterrows()}
        return data_dict


data = get_csv_data("data/french_words.csv")


def get_translation(word_to_translate: str, data):
    translated_word = data.get(word_to_translate)
    canvas.itemconfig(word_text, text=translated_word)


def change_word():
    new_word = choice(list(data.keys()))
    canvas.itemconfig(word_text, text=new_word)


def flip_card():
    canvas.itemconfig(language_text, text="English")
    canvas.itemconfig(word_text)


# Window
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
flash_card_img = tk.PhotoImage(file="./images/card_front.png")
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=flash_card_img)

start_lang = "French"
start_word = "Si"
language_text = canvas.create_text(
    400, 150, text=start_lang, font=("Ariel", 40, "italic")
)
word_text = canvas.create_text(400, 263, text=start_word, font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
checkmark_img = tk.PhotoImage(file="./images/right.png")
checkmark_btn = tk.Button(
    image=checkmark_img, highlightthickness=0, border=0, command=change_word
)
checkmark_btn.grid(column=0, row=1)

wrong_img = tk.PhotoImage(file="./images/wrong.png")
wrong_btn = tk.Button(
    image=wrong_img, highlightthickness=0, border=0, command=change_word
)
wrong_btn.grid(column=1, row=1)

get_translation("laisse", data)

window.mainloop()
