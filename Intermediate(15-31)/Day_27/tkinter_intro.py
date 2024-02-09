import tkinter as tk

window = tk.Tk()
window.title("My TKinter program")
window.minsize(width=500, height=300)

my_label = tk.Label(text="Hi I'm a label!", font=("Arial", 24, "italic"))
my_label.pack(side="right", expand=False)



tk.mainloop()