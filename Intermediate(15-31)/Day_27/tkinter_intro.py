import tkinter as tk

button_counter = 0


def button_clicked():
    global button_counter
    button_counter += 1
    my_label.config(text=f"Clicked {button_counter} times")


window = tk.Tk()
window.title("My TKinter program")
window.minsize(width=500, height=300)

# Label

my_label = tk.Label(text="Hi I'm a label!", font=("Arial", 24, "italic"))
my_label["text"] = "New text"
my_label.config(text="Newer text")
my_label.grid(column=0, row=0)


# Button

button = tk.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# Entry

input = tk.Entry(width=10)
input.grid(column=3, row=2)

button_entry = tk.Button(
    text="Click me too!", command=lambda: my_label.config(text=input.get())
)
button_entry.grid(column=2, row=0)


tk.mainloop()
