from time import sleep
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
reps = 1

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps

    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        text_label.config(text="Break", fg=RED)
        # window.after(LONG_BREAK_MIN * 60 * 1000, start_timer)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        text_label.config(text="Break", fg=PINK)
        # window.after(SHORT_BREAK_MIN * 60 * 1000, start_timer)
    else:
        countdown(WORK_MIN * 60)
        text_label.config(text="Work")
        # window.after(WORK_MIN * 60 * 1000, start_timer)

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count: int):
    minutes: int = count // 60
    seconds: int | str = count % 60
    if len(str(seconds)) == 1:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count <= 0:
        start_timer()
    else:
        window.after(1000, countdown, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Tomato image
tomato_img = tk.PhotoImage(file="./tomato.png")
canvas = tk.Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 111, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(
    FONT_NAME, 28, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Main Label
text_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW,
                      font=(FONT_NAME, 28, "bold"))

text_label.grid(column=1, row=0)

# Start button
start_button = tk.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# Reset button
reset_button = tk.Button(text="Reset")
reset_button.grid(column=2, row=2)

# Check mark label
check_mark_label = tk.Label(
    text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 28, "bold"))

check_mark_label.grid(column=1, row=3)


window.mainloop()
