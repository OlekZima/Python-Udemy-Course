import tkinter as tk
import pandas as pd


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.timer: str = ""

        self.to_learn_df = pd.DataFrame(
            {
                "French": [],
                "English": [],
            }
        )

        self.flip_card_front()

    def init_ui(self):
        self.BACKGROUND_COLOR = "#B1DDC6"
        self.title("Flashy")
        self.config(padx=50, pady=50, bg=self.BACKGROUND_COLOR)
        self.flash_card_front = tk.PhotoImage(file="./images/card_front.png")
        self.flash_card_back = tk.PhotoImage(file="./images/card_back.png")

        self.data: pd.DataFrame = self.get_data(
            "./data/french_words.csv", "./data/words_to_learn.csv"
        )

        self.canvas = tk.Canvas(
            width=800, height=526, bg=self.BACKGROUND_COLOR, highlightthickness=0
        )
        self.canvas_img = self.canvas.create_image(
            400, 263, image=self.flash_card_front
        )

        self.canvas_lang = "French"
        self.canvas_word_french: str = self.data.sample().get("French").to_string(index=False)  # type: ignore

        self.canvas_word_eng = self.get_translation(self.canvas_word_french, self.data)
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
            command=self.checkmark,
        )
        self.checkmark_btn.grid(column=1, row=1)

        self.wrong_img = tk.PhotoImage(file="./images/wrong.png")
        self.wrong_btn = tk.Button(
            image=self.wrong_img,
            highlightthickness=0,
            border=0,
            command=self.wrong,
        )
        self.wrong_btn.grid(column=0, row=1)

    def wrong(self):
        if not self.is_to_learn:
            to_append_df = pd.DataFrame(
                {
                    "French": [self.current_french_word],
                    "English": [
                        self.get_translation(self.current_french_word, self.data)
                    ],
                }
            )
            self.to_learn_df: pd.DataFrame = pd.concat(
                [self.to_learn_df, to_append_df], ignore_index=True
            )
            self.to_learn_df.to_csv("./data/words_to_learn.csv", index=False)
        self.flip_card_front()

    def checkmark(self):
        self.delete_word_from_learning()
        self.flip_card_front()

    def delete_word_from_learning(self):
        if self.is_to_learn:
            data_df = pd.DataFrame(self.data)
            data_df = data_df[data_df["French"] != self.current_french_word]
            data_df.to_csv("./data/words_to_learn.csv", index=False)
            self.data = data_df
        else:
            return

    def change_word(self) -> str:
        try:
            new_word: str = self.data.sample().get("French").to_string(index=False)  # type: ignore
        except ValueError:
            new_word: str = "List is empty!"
        return new_word

    def get_data(self, overall_data: str, words_to_learn_path: str):
        try:
            with open(words_to_learn_path, "r"):
                data = pd.read_csv(words_to_learn_path)
                if data.size == 0:
                    raise FileNotFoundError
                self.is_to_learn = True
                return data
        except FileNotFoundError:
            with open(words_to_learn_path, mode="w"):
                pass
            with open(overall_data, "r"):
                data = pd.read_csv(overall_data)
                self.is_to_learn = False
                return data

    def get_translation(self, word_to_translate: str, data: pd.DataFrame):
        translated_word = data.loc[data["French"] == word_to_translate].get("English").to_string(index=False)  # type: ignore
        return translated_word

    def flip_card_front(self):
        self.canvas.itemconfig(self.language_text, text="French", fill="black")
        self.canvas.itemconfig(self.canvas_img, image=self.flash_card_front)

        self.current_french_word = self.change_word()
        self.canvas.itemconfig(
            self.word_text, text=self.current_french_word, fill="black"
        )

        if self.timer:
            self.after_cancel(self.timer)

        self.timer = self.after(3000, self.flip_card_back)

    def flip_card_back(self):
        self.canvas.itemconfig(self.language_text, text="English", fill="white")
        self.canvas.itemconfig(
            self.word_text,
            text=self.get_translation(
                self.canvas.itemcget(self.word_text, "text"), self.data
            ),
            fill="white",
        )
        self.canvas.itemconfig(self.canvas_img, image=self.flash_card_back)

        self.after_cancel(self.timer)
