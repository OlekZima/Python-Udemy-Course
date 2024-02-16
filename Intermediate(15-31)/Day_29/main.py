import tkinter as tk
from tkinter import messagebox
from random import randint, choice
from string import ascii_letters
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


print("Welcome to the PyPassword Generator!")

pass_len = int(input("How many letters would you like in your password?\n"))
symbols_num = int(input("How many symbols would you like?\n"))
numbers_num = int(input("How many numbers would you like?\n"))

password = ""

for i in range(pass_len):
    password += choice(ascii_letters)

symbols = ['!', '#', '$', '%', '&', '()', ')', '*', '+']

for i in range(symbols_num):
    password += choice(symbols)

for i in range(numbers_num):
    password += str(randint(0, 9))

# password = "".join(sample(password, len(password)))
password = "".join(list(password))

print(f"Your password is {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    website_entry.delete(0, tk.END)

    email = email_entry.get()
    # email_entry.delete(0, tk.END)

    password = password_entry.get()
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
        with open("./data.txt", "a") as f:
            f.write(f"{website} | {email} | {password}\n")
    


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
# window.minsize(240, 240)

# Canvas
lock_image = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Website section
website_label = tk.Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

website_entry = tk.Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

# Email/Username section
email_label = tk.Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)

email_entry = tk.Entry(width=35)
email_entry.insert(tk.END, "name@email.com")
email_entry.grid(row=2, column=1, columnspan=2)

# Password section
password_label = tk.Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1, sticky="E")

generate_pass_btn = tk.Button(text="Generate Password", width=15)
generate_pass_btn.grid(row=3, column=2, sticky="EW")

add_btn = tk.Button(text="Add", width=36, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
