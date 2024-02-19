import json
import tkinter as tk
from tkinter import messagebox
from tkinter import font
from typing import Dict
import pyperclip
from random import randint, choice, shuffle
from string import ascii_letters
from tkinter import ttk
from ttkthemes import ThemedTk


# ----------------------------- PASSWORD SEARCH --------------------------------- #
def find_password():
    website_name = website_entry.get()
    data = read_json_data("./data.json")
    try:
        password = data[website_name]["password"]
    except KeyError:
        messagebox.showerror("Error", "No details for the website exists.")
        return
    else:
        messagebox.showinfo(
            "Password", f"Website: {website_name}\nPassword: {password}"
        )
        pyperclip.copy(password)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, tk.END)

    letters_len = randint(12, 14)
    symbols_num = randint(4, 5)
    numbers_num = randint(4, 5)

    symbols = ["!", "#", "$", "%", "&", "()", ")", "*", "+"]

    password = [choice(ascii_letters) for _ in range(letters_len)]
    password.extend([choice(symbols) for _ in range(symbols_num)])
    password.extend([str(randint(0, 9)) for _ in range(numbers_num)])

    shuffle(password)
    password = "".join(list(password))
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def read_json_data(file_path: str) -> Dict:
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        with open(file_path, "w") as f:
            return {}


def save_data():
    website = website_entry.get()
    website_entry.delete(0, tk.END)

    email = email_entry.get()
    password = password_entry.get()

    data_to_write = {
        website: {
            "email": email,
            "password": password,
        }
    }

    password_entry.delete(0, tk.END)

    if not (website and email and password):
        messagebox.showerror(
            title="Error", message="You must fill all the field before adding data."
        )
        return

    is_user_ok = messagebox.askokcancel(
        title=website,
        message=f"There are the details entered: \nEmail: {email}\nPassword: {password}\nIs ot ok to save?",
    )
    if is_user_ok:
        data = read_json_data("./data.json")
        data.update(data_to_write)
        with open("./data.json", "w") as f:
            json.dump(data, f, indent=4)


# ---------------------------- UI SETUP ------------------------------- #

window = ThemedTk(theme="arc")
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
# window.minsize(240, 240)

# ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
# Canvas
lock_image = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Website section
website_label = tk.Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

website_entry = ttk.Entry(width=25)
website_entry.focus()
website_entry.grid(row=1, column=1, sticky="EW")

search_btn = ttk.Button(text="Search", width=18, command=find_password)
search_btn.grid(row=1, column=2)

# Email/Username section
email_label = tk.Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)

email_entry = ttk.Entry(width=35)
email_entry.insert(tk.END, "name@email.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

# Password section
password_label = tk.Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

password_entry = ttk.Entry(width=25)
password_entry.grid(row=3, column=1, sticky="EW")

generate_pass_btn = ttk.Button(
    text="Generate Password", width=18, command=generate_password,
)
generate_pass_btn.grid(row=3, column=2, sticky="EW")

add_btn = ttk.Button(text="Add", width=36, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
