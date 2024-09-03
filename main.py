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
    "revenue": 0,  # Adding a revenue key to track earnings
}

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Revenue: ${resources['revenue']}")

def check_resources(choice):
    for ingredient in MENU[choice]["ingredients"]:
        if resources[ingredient] < MENU[choice]["ingredients"][ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def check_coins(quarters, dimes, nickels, pennies):
    return quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

if choice in MENU:
    if check_resources(choice):
        quarters = int(input("Enter the number of quarters: "))
        dimes = int(input("Enter the number of dimes: "))
        nickels = int(input("Enter the number of nickels: "))
        pennies = int(input("Enter the number of pennies: "))

        total_money = check_coins(quarters, dimes, nickels, pennies)

        if total_money < MENU[choice]["cost"]:
            print("Sorry, that's not enough money. Money refunded.")
        else:
            resources["revenue"] += MENU[choice]["cost"]
            for ingredient in MENU[choice]["ingredients"]:
                resources[ingredient] -= MENU[choice]["ingredients"][ingredient]

            change = total_money - MENU[choice]["cost"]
            if change > 0:
                print(f"Here is ${change:.2f} in change.")

            print(f"Please enjoy your {choice}.")
    else:
        print("Cannot make the drink due to insufficient resources.")
else:
    print("Invalid choice.")

# Show remaining resources
report()
