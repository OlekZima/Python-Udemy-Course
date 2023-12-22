from typing import Dict, List
import menu_and_resources

class Coffee_machine():
    def __init__(self, initial_resources: Dict[str, int], menu, initital_money: int = 0):
        self._resources = initial_resources
        self._money = initital_money
        self._menu = menu
    

    def print_resources(self) -> None:
        print(f"Water: {self._resources['water']}ml")
        print(f"Milk: {self._resources['milk']}ml")
        print(f"Coffee: {self._resources['coffee']}g")
        print(f"Money: ${self._money}")

    def _get_resources(self) -> List[int]:
        return [self._resources["water"], self._resources["milk"], self._resources["coffee"]]

    @staticmethod
    def _validate_int_input(prompt: str) -> int:
        is_validated = False
        return_val = 0
        while not is_validated:
            try:
                return_val = int(input(prompt))
                if return_val < 0:
                    raise ValueError
                is_validated = True
            except ValueError:
                print("Invalid input!")
        return return_val


    def _reduce_resources(self, water: int, milk: int, coffee: int) -> None:
        self._resources["water"] -= water
        self._resources["milk"] -= milk
        self._resources["coffee"] -= coffee


    def _is_coffee_can_be_made(self, coffee_name: str) -> bool:
        available_resources = self._get_resources()
        ingredients = self._menu[coffee_name]["ingredients"]
        resources_to_spend = [ingredients[key] for key in ingredients]
        availables = [available_resources[i] >= resources_to_spend[i] for i in range(len(available_resources))]
        if False in availables:
            return False
        return True

    def make_coffee(self, coffee_name: str) -> None:
        money = self._count_money()
        coffee = self._menu.get(coffee_name)

        if not self._is_coffee_can_be_made(coffee_name):
            print("Sorry, there is not enough resources for this coffee. Try a different one.")
            return
        
        is_payment_ok = self._process_payment(money, coffee["cost"])
        if not is_payment_ok:
            return
        else:
            ingredients = coffee["ingredients"]    
            self._reduce_resources(ingredients["water"], ingredients["milk"], ingredients["coffee"])
            print(f"Here is your {coffee_name} ☕ Enjoy!")
            self._money += money


    def _process_payment(self, money_to_proceed: float, coffee_price: float) -> bool:
        if money_to_proceed < coffee_price:
            print(f"Sorry that's not enought money. Returning money.")
            return False
        elif money_to_proceed == coffee_price:
            print(f"Payment complete!")
            return True
        else:
            change = round(money_to_proceed - coffee_price, 2)
            print(f"Payment complete! The change is ${change}")
            return True


    def _count_money(self) -> float:
        print("Please insert coins.")
        quarters_val = self._validate_int_input("How many quarters?: ") * 0.25
        dimes_val = self._validate_int_input("How many dimes?: ") * 0.10
        nickles_val = self._validate_int_input("How many nickles?: ") * 0.05
        pennies_val = self._validate_int_input("How many pennies?: ") * 0.01
        if quarters_val * dimes_val * nickles_val * pennies_val < 0:
            print("Invalid money quantity!")
            return 0.0
        else:
            rounded_sum = round(quarters_val + dimes_val + nickles_val + pennies_val, 2)
            return rounded_sum
    

    def get_coffee(self) -> str:
        is_coffee_exists = False
        coffe_to_make = ""
        while not is_coffee_exists:
            coffe_to_make = input("What would you like? (espresso/latte/cappucino): ").lower()
            if coffe_to_make == "report":
                self.print_resources()
            if coffe_to_make in self._menu:
                break
        return coffe_to_make
        


if __name__ == '__main__':
    resources = menu_and_resources.resources
    menu = menu_and_resources.menu
    coffee_machine = Coffee_machine(resources, menu)
    is_working = True
    while is_working:
        try:
            coffee_to_make = coffee_machine.get_coffee()
            coffee_machine.make_coffee(coffee_to_make)
        except:
            print(f"There is an error!")
            print("Shutting down!")
            is_working = False
    
    print("Shutted down")