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
    "water": 3000,
    "milk": 200,
    "coffee": 100,
    "profit": 0,
}


def report():
    print("\n----- MACHINE REPORT -----")
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Profit: ${resources['profit']:.2f}")
    print("--------------------------")


def show_menu():
    print("\n---------- MENU ----------")
    print("Espresso   - $1.50")
    print("Latte      - $2.50")
    print("Cappuccino - $3.00")
    print("--------------------------")
    print("Other commands: 'report', 'menu', or 'off'")


def check_resources(choice):
    for ingredient in MENU[choice]["ingredients"]:
        amount_needed = MENU[choice]["ingredients"][ingredient]

        if resources[ingredient] < amount_needed:
            print(f"Sorry, there is not enough {ingredient}.")
            return False

    return True


def process_coins():
    print("\nEnter the money! 🪙")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    money = (
        0.25 * quarters
        + 0.10 * dimes
        + 0.05 * nickels
        + 0.01 * pennies
    )

    return money


def check_money(choice, money):
    price = MENU[choice]["cost"]

    if money < price:
        print("Not enough money! Your money has been refunded. 🙅🏼💵")
        return False

    elif money > price:
        change = money - price
        print(f"Here is ${change:.2f} in change.")

    resources["profit"] += price
    return True


def make_coffee(choice):
    print("\nMaking your coffee. Please wait! ☕")

    for ingredient in MENU[choice]["ingredients"]:
        resources[ingredient] -= MENU[choice]["ingredients"][ingredient]

    print(f"Here is your {choice}. Enjoy! ☕")


print("Welcome to the Coffee Machine! ☕")

ask = input("Would you like to turn on the machine? (yes/no):\n").lower().strip()

if ask == "yes":
    machine_on = True
else:
    machine_on = False
    print("No problem. Have a nice day! 👋")


while machine_on:

    choice = input(
        "\nWhat can I do for you?\n"
        "Choose espresso, latte, cappuccino, menu, report, or off:\n"
    ).lower().strip()

    if choice == "off":
        print("Turning off the coffee machine. Goodbye! 👋")
        machine_on = False

    elif choice == "report":
        report()

    elif choice == "menu":
        show_menu()

    elif choice in MENU:
        if check_resources(choice):
            money = process_coins()
            print(f"You inserted: ${money:.2f}")

            if check_money(choice, money):
                make_coffee(choice)

    else:
        print("Sorry, I don't understand that option.")
        show_menu()