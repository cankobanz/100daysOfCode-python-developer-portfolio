from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("U.S State Game")
image_path = "blank_states_img.gif"
screen.bgpic(image_path)

df = pd.read_csv("50_states.csv")
all_states = df["state"].to_list()

count_correct = 0
correct_guesses = []
while True:
    answer_state = screen.textinput(title=f"{count_correct}/50 States Correct", prompt="What is the next state name?")
    answer_state = answer_state.title()
    current_column = df[df["state"] == answer_state]
    if answer_state == "Exit":
        break
    if answer_state in all_states and answer_state not in correct_guesses:
        count_correct += 1
        correct_guesses.append(answer_state)
        x = int(current_column["x"])
        y = int(current_column["y"])

        t = Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x, y)
        t.write(answer_state)

pd.DataFrame({
    "states": [item for item in all_states if item not in correct_guesses]
}).to_csv("states_to_learn.csv")

screen.exitonclick()
