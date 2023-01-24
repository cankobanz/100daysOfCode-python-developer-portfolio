from tkinter import *
from tkinter import messagebox
from random import  randint, choice, shuffle
import json

YELLOW = "#f7f5dd"
FONT_NAME = "Times New Roman"

letters = ['a', 'b', 'c', 'hour_data', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    try:
        with open("data.json", mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found Error", message="No Data File Found!")
    else:
        website = entry_website.get()
        try:
            email_password = data[website]
        except KeyError:
            messagebox.showinfo(title="Key Error", message="No details for the website exists.")
        else:
            email = email_password["email"]
            password = email_password["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_letters = [choice((letters)) for _ in range(randint(8, 10))]
    password_symbols = [choice((symbols)) for _ in range(randint(2, 4))]
    password_numbers = [choice((numbers)) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if email == "" or password == "":
        messagebox.showinfo(title="Warning!",message="Either your email or password is empty!\n"
                                                     "Please enter something.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                      f"Email: {email}\nPassword{password}\n"
                                                      f"Is it ok to save?")
        if is_ok:
            try:
                with open("data.json", mode='r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", mode='w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode='w') as file:
                    json.dump(data, file, indent=4)
            finally:
                entry_website.delete(0, END)
                entry_password.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
logo = PhotoImage(file="../day29-PasswordManager/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
label_website = Label(text="Website:", font=(FONT_NAME, 13, "bold"), bg=YELLOW)
label_website.grid(row=1, column=0)
label_email = Label(text="Email/Username:", font=(FONT_NAME, 13, "bold"), bg=YELLOW)
label_email.grid(row=2, column=0)
label_password = Label(text="Password:", font=(FONT_NAME, 13, "bold"), bg=YELLOW)
label_password.grid(row=3, column=0)

# Entries
entry_website = Entry(width=35)
entry_website.insert(0, "Amazon")
entry_website.grid(row=1, column=1, columnspan=2)
entry_email = Entry(width=35)
entry_email.insert(0, "can@gmail.com")
entry_email.grid(row=2, column=1, columnspan=2)
entry_password = Entry(width=21)
entry_password.insert(0, "password")
entry_password.grid(row=3, column=1)

# Buttons
button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(row=3, column=2)
button_add = Button(text="Add", command=save, width=36)
button_add.grid(row=4, column=1, columnspan=2)
button_search = Button(text="Search", command=search)
button_search.grid(row=1, column=2)

window.mainloop()
