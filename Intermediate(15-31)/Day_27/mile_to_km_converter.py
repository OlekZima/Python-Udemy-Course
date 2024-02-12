import tkinter as tk

window = tk.Tk()
window.title("Mile to km Converter")
window.minsize(width=300, height=200)

entry_miles = tk.Entry()
entry_miles.config(width=10)
entry_miles.config(takefocus=True)
entry_miles.grid(column=1, row=0)


tk.mainloop()
