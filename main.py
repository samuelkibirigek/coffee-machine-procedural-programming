
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
money = 0
profit = 0

# TODO: 1. Print a report of all coffee resources.

def report():
    print(f'water = {resources["water"]}\nmilk = {resources["milk"]}\ncoffee = {resources["coffee"]}\nprofit = {profit}')

# TODO: 2. Check resources sufficient.
def sufficient():
    for coffee in MENU:
        if choice == coffee:
            for ing in MENU[choice]["ingredients"]:
                if ing in resources:
                    try:
                        assert MENU[choice]["ingredients"][ing] > resources[ing]
                    except AssertionError:
                        print("Ingredients not enough")
                        break


# TODO: 3. Process coins.
def coins():
    quater = int(input("How many quaters:"))
    dimes = int(input("How many dimes:"))
    nickel = int(input("How many nickels:"))
    pennies = int(input("How many pennies:"))

    global money
    money = ((quater*0.25)+(dimes*0.10)+(nickel*0.05)+(pennies*0.01))

    return money

# TODO: 4. Check transaction is successful.

def transaction():

    if money > MENU[choice]["cost"]:
        enough_ingredients = True
        for ing in MENU[choice]["ingredients"]:
            try:
                assert MENU[choice]["ingredients"][ing] < resources[ing]
            except AssertionError:
                print("Not enough resources.")
                enough_ingredients = False
                break
        if enough_ingredients:
            balance = money - MENU[choice]["cost"]
            global profit
            profit += MENU[choice]["cost"]

            if balance > 0:
                print(f"Here is ${round(balance, 2)} in change.")

            for ing in MENU[choice]["ingredients"]:
                resources[ing] -= MENU[choice]["ingredients"][ing]


    else:
        print("Sorry that's not enough money. Money refunded.")


coins()
transaction()
report()
