import random

from art import logo, vs
from game_data import data

print(logo)


# Randomly choose two elements
def select_element():
    return random.choices(data)[0]


def print_element(element):
    return f"{element['name']}, {element['description']}, from {element['country']}."


def compare_elements(a, b):
    if a['follower_count'] > b['follower_count']:
        return "A"
    else:
        return "B"


score = 0
end_of_game = True
while end_of_game:
    a_element = select_element()
    b_element = select_element()
    # Compare those two elements with words VS
    print("Compare A: " + print_element(a_element) + "\n" + vs + "\nAgainst B: " + print_element(b_element))
    user_answer = input("Who has more followers? Type 'A' or 'B':")

    # Compare those two elements with in terms of followers
    answer = compare_elements(a_element, b_element)
    # Ask user "Who has more followers? Type 'A' or 'B':"
    if user_answer != "A" and user_answer != "B":
        print("Please, Type A or B.")
        continue
    # If the user guesses correct, increase score one ask again
    if answer == user_answer:
        score += 1
        print(f"Current score is: {score}")
    else:
        end_of_game = False
    # Ask until answer is incorrect.

# Report the score
print(f"Final score is {score}!")
