from cgitb import text
import tkinter as tk
import requests


class Window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.config(padx=50, pady=50)
        self.title("Kanye Says...")

        self.background = tk.PhotoImage(file="background.png")
        self.canvas = tk.Canvas(width=300, height=414)
        self.canvas.create_image(150, 207, image=self.background)
        self.quote_text = self.canvas.create_text(
            150, 207, text="Quote", width=250, font=("Arial", 20, "bold"), fill="white"
        )
        self.canvas.grid(row=0, column=0)
        self.get_quote()

        self.kanye = tk.PhotoImage(file="kanye.png")
        self.button = tk.Button(
            image=self.kanye, highlightthickness=0, command=self.get_quote
        )
        self.button.grid(row=1, column=0)

    def get_quote(self):
        response = requests.get("https://api.kanye.rest/text")
        response.raise_for_status()
        # data_json = response.json()
        # quote = data_json["quote"]
        quote = response.text
        self.canvas.itemconfig(self.quote_text, text=quote)


if __name__ == "__main__":
    window = Window()
    window.mainloop()
