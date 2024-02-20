from cgitb import text
from random import choice
import tkinter as tk
import pandas as pd
from typing import Dict


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.BACKGROUND_COLOR = "#B1DDC6"
        self.title("Flashy")
        self.config(padx=50, pady=50, bg=self.BACKGROUND_COLOR)
        self.flash_card_front = tk.PhotoImage(file="./images/card_front.png")
        self.flash_card_back = tk.PhotoImage(file="./images/card_back.png")

        self.data_dict: Dict[str, str] = self.get_data("./data/french_words.csv")

        self.canvas = tk.Canvas(
            width=800, height=526, bg=self.BACKGROUND_COLOR, highlightthickness=0
        )
        self.canvas_img = self.canvas.create_image(
            400, 263, image=self.flash_card_front
        )

        self.canvas_lang = "French"
        self.canvas_word_french = choice(list(self.data_dict.keys()))
        self.canvas_word_eng = self.get_translation(
            self.canvas_word_french, self.data_dict
        )
        self.language_text = self.canvas.create_text(
            400, 150, text=self.canvas_lang, font=("Ariel", 40, "italic")
        )
        self.word_text = self.canvas.create_text(
            400, 263, text=self.canvas_word_french, font=("Ariel", 60, "bold")
        )
        self.canvas.grid(column=0, row=0, columnspan=2)

        # Buttons
        self.checkmark_img = tk.PhotoImage(file="./images/right.png")
        self.checkmark_btn = tk.Button(
            image=self.checkmark_img,
            highlightthickness=0,
            border=0,
            command=self.flip_card_front,
        )
        self.checkmark_btn.grid(column=0, row=1)

        self.wrong_img = tk.PhotoImage(file="./images/wrong.png")
        self.wrong_btn = tk.Button(
            image=self.wrong_img,
            highlightthickness=0,
            border=0,
            command=self.flip_card_back,
        )
        self.wrong_btn.grid(column=1, row=1)

        self.timer = self.after(3000, self.flip_card_back)

    def change_word(self):
        new_word = choice(list(self.data_dict.keys()))
        return new_word

    def get_data(self, path: str) -> Dict[str, str]:
        try:
            with open(path, "r"):
                data = pd.read_csv(path)
                data_dict = {
                    row["French"]: row["English"] for (_, row) in data.iterrows()
                }
                return data_dict
        except FileNotFoundError:
            return {}

    def get_translation(self, word_to_translate: str, data: Dict[str, str]):
        translated_word = data.get(word_to_translate, "None")
        return translated_word

    def flip_card_back(self):
        self.canvas.itemconfig(self.language_text, text="English", fill="white")
        self.canvas.itemconfig(
            self.word_text,
            text=self.get_translation(
                self.canvas.itemcget(self.word_text, "text"), self.data_dict
            ),
            fill="white",
        )

        self.canvas.itemconfig(self.canvas_img, image=self.flash_card_back)
        self.after_cancel(self.timer)

        # self.canvas.itemconfig(self.word_text, text=self.get_translation())

    def flip_card_front(self):
        self.canvas.itemconfig(self.language_text, text="French", fill="black")
        self.canvas.itemconfig(self.word_text, text=self.change_word(), fill="black")

        self.canvas.itemconfig(self.canvas_img, image=self.flash_card_front)


if __name__ == "__main__":
    window = Window()
    window.mainloop()
