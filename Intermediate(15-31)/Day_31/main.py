import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"

# Window
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
flash_card_img = tk.PhotoImage(file="./images/card_front.png")
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=flash_card_img)

language_text = "French"
word_text = "trouve"
canvas.create_text(400, 150, text=language_text, font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text=word_text, font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
checkmark_img = tk.PhotoImage(file="./images/right.png")
checkmark_btn = tk.Button(image=checkmark_img, highlightthickness=0, border=0)
checkmark_btn.grid(column=0, row=1)

wrong_img = tk.PhotoImage(file="./images/wrong.png")
wrong_btn = tk.Button(image=wrong_img, highlightthickness=0, border=0)
wrong_btn.grid(column=1, row=1)


window.mainloop()
