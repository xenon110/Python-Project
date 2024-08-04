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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#
# user = str(input("please type resources to see the resources avilable in machine "))
#     if user == "report":
#         print(MENU["resources"])
def is_resource_sufficient(order_ingrdient):
    for item in order_ingrdient:
        if order_ingrdient[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def coin():
    print("please insert the coin: ")
    total = int(input("Insert the quarters: "))*0.025
    total += int(input("Insert the dimes: "))*0.10
    total += int(input("Insert the nickels: "))*0.05
    total += int(input("Insert the pennies: "))*0.01
    return total


def transition_sucessfull(money_recieved,drink_cost):
    if money_recieved >= drink_cost:
        change=money_recieved-drink_cost
        print(f"Here is your change ${change} ")
        return True
    else:
        print("Sorry your money is insufficient ")
        return False


def make_coffee(drink_name,order_ingrdient):
    """" Dedect the ingrideant from the resources """
    for item in order_ingrdient:
        resources[item] -= order_ingrdient
    print(f"Here is your {drink_name} ")

is_on=True

while is_on:
    choice=input("What would you like? (espresso/latte/cappuccino): ")
    if choice=="off":
        is_on = False
    elif choice=="report":
        print(f"Water {resources['water']}ml")
        print(f"Milk {resources['milk']}ml")
        print(f"coffee {resources['coffee']}mg")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = coin()
            if transition_sucessfull(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



