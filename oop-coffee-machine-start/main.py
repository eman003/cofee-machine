from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_off = False
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
while not is_off:
    choice = input(f"What would you like? ({menu.get_items()}): ")

    if choice == "off":
        print("G00dby3!")
        is_off = True
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
