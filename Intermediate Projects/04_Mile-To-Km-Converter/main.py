from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 16, "normal"))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial", 16, "normal"))
equal_label.grid(column=0, row=1)

km_value = Label(text="0", width=8, font=("Arial", 18, "bold"))
km_value.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 16, "normal"))
km_label.grid(column=2, row=1)


def calculate_km():
    km = round(float(miles_entry.get()) * 1.609, 3)
    km_value.config(text=km)


button = Button(text="Calculate", command=calculate_km)
button.grid(column=1, row=2)


window.mainloop()