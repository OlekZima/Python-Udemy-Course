import tkinter as tk


def main():

    def key_callback(event):
        convert_miles_to_km()

    def convert_miles_to_km():
        miles: float = float(entry_miles.get())
        km: float = round(miles * 1.609344, 2)
        label_converted_km.config(text=str(km))

    window = tk.Tk()
    window.title("Mile to km Converter")
    window.bind(sequence="<Return>", func=key_callback)
    window.minsize(width=170, height=120)
    window.config(padx=10, pady=20)

    entry_miles = tk.Entry(width=10, takefocus=True)
    entry_miles.grid(column=1, row=0)

    label_miles = tk.Label(text="Miles")
    label_miles.grid(column=2, row=0)

    info_label = tk.Label(text="Is equal to")
    info_label.grid(column=0, row=1)

    label_converted_km = tk.Label(text="0")
    label_converted_km.grid(column=1, row=1)

    label_km = tk.Label(text="km")
    label_km.grid(column=2, row=1)

    button_calculate = tk.Button(text="Calculate", command=convert_miles_to_km)
    button_calculate.grid(column=1, row=2)

    tk.mainloop()


if __name__ == "__main__":
    main()
