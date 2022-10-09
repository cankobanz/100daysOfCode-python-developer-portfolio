import random

from art import logo

print(logo)


def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user = [random.choice(cards), random.choice(cards)]
    computer = [random.choice(cards), random.choice(cards)]

    is_card_drawn = True
    computer_point = sum(computer)
    while is_card_drawn:
        user_point = sum(user)

        if user_point == 21:
            print(f"User cards: {user}")
            print(f"Computer cards: {computer}")
            return "Win"
        elif computer_point == 21:
            print(f"User cards: {user}")
            print(f"Computer cards: {computer}")
            return "Lose"

        if user_point > 21:
            if 11 in user:
                user.remove(11)
                user.append(1)
                user_point = sum(user)
                if user_point > 21:
                    print(f"User cards: {user}")
                    print(f"Computer cards: {computer}")
                    return "Lose"
            else:
                print(f"User cards: {user}")
                print(f"Computer cards: {computer}")
                return "Lose"

        print(f"User cards: {user}")
        print(f"Computer cards: {computer}")
        if input("Do you want to another card? 'y' or 'n'.\n") == "y":
            user.append(random.choice(cards))
        else:
            is_card_drawn = False

    while computer_point < 17:
        computer.append(random.choice(cards))
        computer_point = sum(computer)
        if computer_point > 21:
            print(f"User cards: {user}")
            print(f"Computer cards: {computer}")
            return "Win"

    if user_point > computer_point:
        print(f"User cards: {user}")
        print(f"Computer cards: {computer}")
        return "Win"
    elif user_point < computer_point:
        print(f"User cards: {user}")
        print(f"Computer cards: {computer}")
        return "Lose"
    else:
        print(f"User cards: {user}")
        print(f"Computer cards: {computer}")
        return "Draw"

print(blackjack())
