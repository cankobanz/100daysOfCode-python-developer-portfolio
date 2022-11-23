import tkinter as tk


def button_clicked():
    km_val = round(1.689 * float(entry.get()))
    answer.config(text=km_val)


window = tk.Tk()
window.title("First GUI")
window.config(padx=20, pady=20)


answer = tk.Label(text=0, font=("Ariel", 16))
answer.grid(row=1, column=1)

is_equal_to = tk.Label(text="is equal to", font=("Ariel", 16))
is_equal_to.grid(row=1, column=0)

miles = tk.Label(text="Miles", font=("Ariel", 16))
miles.grid(row=0, column=2)

km = tk.Label(text="km", font=("Ariel", 16))
km.grid(row=1, column=2)

button = tk.Button(text="Click me", command=button_clicked)
button.grid(row=2, column=1)

entry = tk.Entry(width=15)
entry.grid(row=0, column=1)

window.mainloop()
