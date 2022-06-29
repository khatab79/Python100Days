from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

power_machine = "on"

coffee_menu = Menu()

my_coffee_machine = CoffeeMaker()

money = MoneyMachine()

   
def coffee_machine():

    choice = input(f"  What would you like? ({coffee_menu.get_items()}): ").lower()
    while power_machine == "on":
        if (choice == "off"):
            return power_machine == "off"
        elif (choice == "report"):
            my_coffee_machine.report()
            money.report()
        else:
            order = coffee_menu.find_drink(choice)
            is_resources_enough = my_coffee_machine.is_resource_sufficient(order)
            if is_resources_enough:
                is_payment_ok = money.make_payment(coffee_menu.find_drink(choice).cost)
                if is_payment_ok:
                   my_coffee_machine.make_coffee(order)
        choice = input("  What would you like? (espresso/latte/cappuccino): ").lower()

coffee_machine()