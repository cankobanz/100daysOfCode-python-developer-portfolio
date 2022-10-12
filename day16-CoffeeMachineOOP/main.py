from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee_machine = CoffeeMaker()
money_machine_object = MoneyMachine()
menu_object = Menu()

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_machine.report()
    else:
        drink = menu_object.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink):
            cost = drink.cost
            if money_machine_object.make_payment(cost):
                coffee_machine.make_coffee(drink)


