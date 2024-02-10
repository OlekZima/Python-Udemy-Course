import tkinter as tk

window = tk.Tk()
window.title("My TKinter program")
window.minsize(width=500, height=300)

# Label

my_label = tk.Label(text="Hi I'm a label!", font=("Arial", 24, "italic"))
my_label.pack()

my_label["text"] = "New text"
my_label.config(text="Newer text")

# Button

counter = 0


def button_clicked():
    global counter
    counter += 1
    my_label.config(text=f"Clicked {counter} times")


button = tk.Button(text="Click me", command=button_clicked)
button.pack()

# Entry

input = tk.Entry(width=10)
input.pack()

button_entry = tk.Button(
    text="Click me too!", command=lambda: my_label.config(text=input.get())
)
button_entry.pack()


tk.mainloop()
