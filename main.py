MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

PENNY = 0.01
NICKEL = 0.05
DIME = 0.1
QUARTER = 0.25


def check_resources(coffee_type):
    """
    checks if the coffee machine have enough ingredients
    :param coffee_type:
    :return bool:
    """
    water = resources["water"]
    required_water = MENU[coffee_type]["ingredients"]["water"]
    coffee = resources["water"]
    required_coffee = MENU[coffee_type]["ingredients"]["water"]

    if coffee_type != "espresso":
        milk = resources["milk"]
        required_milk = MENU[coffee_type]["ingredients"]["milk"]
        if water < required_water:
            return "Water"
        elif milk < required_milk:
            return "Milk"
        elif coffee < required_coffee:
            return "Coffee"
    else:
        if water < required_water:
            return "Water"
        elif coffee < required_coffee:
            return "Coffee"
        else:
            return False


def process_coins(inserted_quarter, inserted_dimes, inserted_nickels, inserted_pennies):
    """
    returns total amount of the coins inserted:
    :return float
    """

    total_quarter_amount = (inserted_quarter * QUARTER)
    total_dimes_amount = (inserted_dimes * DIME)
    total_nickels_amount = (inserted_nickels * NICKEL)
    total_pennies_amount = (inserted_pennies * PENNY)

    return total_quarter_amount + total_dimes_amount + total_nickels_amount + total_pennies_amount


def process_resources(coffee_type):
    """
    Deducts used resources and returns remaining resources
    :param coffee_type:
    :return dict:
    """
    remaining_ingredients = {
        "water": resources["water"] - MENU[coffee_type]["ingredients"]["water"],
        "coffee": resources["coffee"] - MENU[coffee_type]["ingredients"]["coffee"],
        "milk": resources['milk']
    }
    if coffee_type != 'espresso':
        remaining_ingredients["milk"] = resources["milk"] - MENU[coffee_type]["ingredients"]["milk"]

    return remaining_ingredients


def make_coffee(inserted_quarter, inserted_dimes, inserted_nickels, inserted_pennies, which_coffee):
    """
    Makes coffee and updates resources
    :param inserted_quarter:
    :param inserted_dimes:
    :param inserted_nickels:
    :param inserted_pennies:
    :param which_coffee:
    :return dict:
    """
    coffee_cost = MENU[which_coffee]["cost"]
    coins = process_coins(inserted_quarter, inserted_dimes, inserted_nickels, inserted_pennies)
    if coins >= coffee_cost:
        print(f"Here is ${round(coins - coffee_cost, 2)} in change")
        print(f"Here is  your {which_coffee} ☕. Enjoy")
        local_resource = process_resources(which_coffee)
        local_resource["money"] = coffee_cost
        return {
            "resources": local_resource,
            "success": True
        }
    else:
        print("Sorry that's not enough money")
        print(f"Here is your money back ${round(coins, 2)}")
        return resources


def checks_if_command_is_valid(entered_command, restart):
    """
    Checks if the user entered a valid command.
    :param entered_command:
    :param restart:
    :return:
    """
    commands = MENU
    commands["report"] = True
    commands["-r"] = True
    commands["off"] = True
    commands["help"] = True
    commands["-h"] = True

    if entered_command not in commands:
        print(f"We don't offer {entered_command} functionality.")
        restart()


def report():
    """
    prints out the report of all the resources and money
    :return dict:
    """
    reports = {}
    for resource in resources:
        if resource == "water" or resource == "milk":
            reports[resource] = f"{resource.title()}: {str(resources[resource])}ml"
        elif resource == "coffee":
            reports[resource] = f"{resource.title()}: {str(resources[resource])}g"
        else:
            reports[resource] = f"{resource.title()}: ${str(round(resources[resource],2))}"
    return reports


def available_commands():
    """ prints available command """
    print("Below is the available commands you can use")
    print("espresso")
    print("latte")
    print("cappuccino")
    print("-r | report")
    print("off")


def validate_coin(coin):
    if coin == "":
        return 0
    else:
        return int(coin)


def coffee_machine():
    command = input("What would you like? (espresso/latte/cappuccino): ").lower()
    checks_if_command_is_valid(command, coffee_machine)
    if command == 'off':
        print("Goodbye!")
        return
    elif command == "report" or command == "-r":
        for resource in resources:
            print(report()[resource])
        coffee_machine()
    elif command == "help" or command == "-h":
        available_commands()
        coffee_machine()
    else:
        if not check_resources(command):
            print("Please insert coins.")
            inserted_quarter = validate_coin(input("how many quarters?: "))
            inserted_dimes = validate_coin(input("how many dimes?: "))
            inserted_nickels = validate_coin(input("how many nickels?: "))
            inserted_pennies = validate_coin(input("how many pennies?: "))

            coffee_done = make_coffee(inserted_quarter, inserted_dimes, inserted_nickels, inserted_pennies, command)

            if "success" in coffee_done and coffee_done["success"]:
                resources["water"] = coffee_done["resources"]["water"]
                resources["milk"] = coffee_done["resources"]["milk"]
                resources["coffee"] = coffee_done["resources"]["coffee"]
                resources["money"] += coffee_done["resources"]["money"]
        else:
            print(f"Sorry there is not enough {check_resources(command)}")
        coffee_machine()


coffee_machine()
