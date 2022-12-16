from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"


def right():
    pass


def wrong():
    pass

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    card_info = original_data.to_dict(orient="records")
else:
    card_info = df.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    current_card = random.choice(card_info)
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=card_back)


def is_known():
    card_info.remove(current_card)
    data = pandas.DataFrame(card_info)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Learn New Words")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="../day31-CardAppCapstoneProject/images/card_front.png")
card_back = PhotoImage(file="../day31-CardAppCapstoneProject/images/card_back.png")
card_image = canvas.create_image(400, 270, image=card_front)
card_title = canvas.create_text(400, 150, fill="black", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

image_right = PhotoImage(file="../day31-CardAppCapstoneProject/images/right.png")
button_right = Button(image=image_right, command=is_known, highlightthickness=0)
button_right.grid(row=1, column=0)

image_wrong = PhotoImage(file="../day31-CardAppCapstoneProject/images/wrong.png")
button_wrong = Button(image=image_wrong, command=next_card, highlightthickness=0)
button_wrong.grid(row=1, column=1)

next_card()

window.mainloop()
