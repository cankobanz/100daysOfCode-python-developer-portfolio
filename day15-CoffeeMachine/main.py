from machine_data import resources, MENU


def calculate_money(quarters, dimes, nickels, pennies):
    return round((quarters * 25 + dimes * 10 + nickels * 5 + pennies * 1)/100, 2)


def is_available(order_ingredients):
    """Checks resources in the machine sufficient or not to make the order."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, we're running out of {item}.")
            return False
        print("Here is your coffee! ☕️Enjoy.")
        return True


def is_money_enough(money, cost):
    if money >= cost:
        return True
    else:
        return False


def calculate_change(money, cost):
    return money - cost


def make_coffee(order_ingredients):
    for item in order_ingredients:
        resources[item] = resources[item] - order_ingredients[item]


def coffee_machine():
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        else:
            if choice != "espresso" and choice != "latte" and choice != "latte":
                print("Please, print either espresso/latte/cappuccino")
                continue
            order = MENU[choice]

            print("Please, insert coins.")
            user_money = calculate_money(int(input("how many quarters?: ")), int(input("how many dimes?: ")),
                                         int(input("how many nickles?: ")), int(input("how many pennies?: ")))

            if is_money_enough(user_money, order["cost"]):
                if is_available(order["ingredients"]):
                    make_coffee(order["ingredients"])
                else:
                    continue
                print("Here is %.2f in change." %calculate_change(user_money, order["cost"]))
            else:
                print("Sorry that's not enough money. Money refunded.")
                continue


coffee_machine()
