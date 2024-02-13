import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = tk.PhotoImage(file="./tomato.png")
canvas = tk.Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 111, image=tomato_img)
canvas.create_text(100, 130, text="00:00", font=(
    FONT_NAME, 28, "bold"), fill="white")
canvas.pack()

window.mainloop()
