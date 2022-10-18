import random
from turtle import Turtle, Screen


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

if user_bet:
    is_race_on = True

y_coord = -100
all_turtles = []
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    all_turtles.append(new_turtle)
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-y_coord)
    y_coord += 40

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.position()[0] >= 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You win! {winner_color} is the winner!")
            else:
                print(f"You lost! {winner_color} is the winner!")



screen.exitonclick()
