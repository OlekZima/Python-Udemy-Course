import tkinter as tk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    data = f"{website} | {email} | {password}"

    with open("./data.txt", "a") as f:
        f.write(data)


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

generate_pass_btn = tk.Button(text="Generate Password")
generate_pass_btn.grid(row=3, column=2)

add_btn = tk.Button(text="Add", width=36, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
