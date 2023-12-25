from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def overall_report():
    coffee_machine.report()
    money_machine.report()


def validate_user_str_input(prompt: str) -> MenuItem:
    is_validated = False
    while not is_validated:
        user_input = input(prompt).lower()
        if user_input == "report":
            overall_report()
            continue
        check_input = coffee_menu.find_drink(user_input)
        if isinstance(check_input, MenuItem):
            return check_input
    return MenuItem("", 0, 0, 0, 0.0)


def coffee_maker():
    is_coffee = True
    while is_coffee:
        coffee_to_make = validate_user_str_input(f"What would you like? ({coffee_menu.get_items()}): ")
        is_resources = coffee_machine.is_resource_sufficient(coffee_to_make)
        if not is_resources:
            continue
        else:
            is_payment_ok = money_machine.make_payment(coffee_to_make.cost)
            if is_payment_ok:
                coffee_machine.make_coffee(coffee_to_make)


if __name__ == '__main__':
    coffee_menu = Menu()
    coffee_machine = CoffeeMaker()
    money_machine = MoneyMachine()
    coffee_maker()