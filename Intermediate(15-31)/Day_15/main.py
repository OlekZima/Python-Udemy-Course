from typing import Dict

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


def print_resources(resources: Dict[str, int], money: float) -> None:
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def validate_int_input(prompt: str) -> int:
    is_validated = False
    return_val = 0
    while not is_validated:
        try:
            return_val = int(input(prompt))
            if return_val < 0:
                continue
            is_validated = True
        except ValueError:
            print("Invalid input!")
    return return_val


def reduce_resources(water: int, milk: int, coffee: int) -> None:
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee

def make_coffee(coffee: Dict) -> float:
    money = count_money(coffee["cost"])
    if money != 0:
        ingredients = coffee["ingredients"]
        reduce_resources(ingredients["water"], ingredients["milk"], ingredients["coffee"])
        return money


def count_money(coffee_price: float):
    print("Please insert coins.")
    quarters_val = validate_int_input("How many quarters?: ") * 0.25
    dimes_val = validate_int_input("How many dimes?: ") * 0.10
    nickles_val = validate_int_input("How many nickles?: ") * 0.05
    pennies_val = validate_int_input("How many pennies?: ") * 0.01
    money = quarters_val + dimes_val + nickles_val + pennies_val
    if money < coffee_price:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    else:
        change = round(money - coffee_price, 2)
        print(f"Here is ${change} in change.")
        return coffee_price


def coffee_machine() -> None:
    overall_money = 0.0


if __name__ == '__main__':
    count_money(2.5)