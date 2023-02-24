
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
}

choice = input("What coffee would you like please: \n").lower()

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

# TODO: 1. Print a report of all coffee resources.

def report():
    print(f"water = {water}\nmilk = {milk}\ncoffee = {coffee}")



# TODO: 2. Check resources sufficient.
def sufficient():
    for coffee in MENU:
        if choice == coffee:
            ing = MENU[choice]["ingredients"]
            print(ing)


sufficient()

# TODO: 3. Process coins.

# TODO: 4. Check transaction is successful.




