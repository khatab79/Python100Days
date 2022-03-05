from data import resources, MENU
# 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino)
    # The prompt should show every time action has completed
    # The prompt should show again to serve the next customer.

# coins = {
#     "quarters": 0.25,
#     "dimes": 0.10,
#     "nickles": 0.05,
#     "pennies": 0.01,
# }
#
PENNIE = 0.01
NICKLE =  0.05
DIME = 0.10
QUARTER = 0.25




power_machine = "on"

water = resources["water"]
milk = resources["milk"]
coffee  = resources["coffee"]

money_in_bank  = 0.00

# 2. Turn off the Coffee Machine by entering “ off ” to the prompt
def turn_off ():
    return "off"

# 3. Print report. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. 
    # e.g.
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5
def report():  
    return f"Water: { water }ml\nMilk: { milk }ml\nCoffee: { coffee }g\nMoney: ${ round(float(money_in_bank), 2) }"


# 4. Check resources sufficient
    # should check if there are enough resources to make that drink.
    # if any resource is deplete. print: “ Sorry there is not enough resource (water, ....etc ). ”
def check_resources(choice):
    is_resources = True
    global water  
    global milk
    global coffee
    
    sufficient_resources = []

    if "water" in MENU[choice]['ingredients']:
        if water < MENU[choice]['ingredients']["water"] :
            is_resources = False        
            sufficient_resources.append("Water") 
    
    if "milk" in MENU[choice]['ingredients']:
        if milk < MENU[choice]['ingredients']["milk"]:
            is_resources = False        
            sufficient_resources.append("milk") 

    if "coffee" in MENU[choice]['ingredients']:
        if coffee < MENU[choice]['ingredients']["coffee"]:
            is_resources = False        
            sufficient_resources.append("coffee")        
    
    if not is_resources:
        msg = "Sorry there is not enough : "
        for sufficient in sufficient_resources:
             msg += sufficient + ", "    
        print(msg.strip(", "))
    return is_resources

# 6. Check transaction successful
    # Check that the user has inserted enough money to purchase the drink they selected.
        # after counting the coins the program should say
            # user has inserted enough money, the cost of the drink gets added to the machine as the profit
                # this will be reflected the “report” 
            # or “ Sorry that's not enough money. Money refunded. ”
    # user has inserted too much money, the machine should offer change (rounded to 2 decimal)
def check_money (money, choice):
    global money_in_bank
    _money = round(money - MENU[choice]['cost'], 2)
    if money >= 0:
        money_in_bank += round(money, 2)
    return _money
    
# 5. Process coins
    # If there are sufficient resources to make the drink selected, the program should prompt the user to insert coins.
        # quarters = $0.25 
        # dimes = $0.10
        # nickles = $0.05
        # pennies = $0.01
    # Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
    # pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
def process_coins():
    print("Please insert coins.")
    money = int(input ("how many quarters?: ")) * QUARTER 
    money += int(input ("how many dimes?: ")) * DIME
    money += int(input ("how many nickles?: ")) * NICKLE
    money += int(input ("how many pennies?: ")) * PENNIE
    
    return round(float(money), 2)


# 7. Make Coffee
    # If the transaction is successful and there are enough resources to make the drink the user selected
    # the ingredients to make the drink should be deducted from the coffee machine resources.
    # Once all resources have been deducted, tell the user “Here is your "choice of drink". Enjoy!”
def make_coffee(money, choice):
    change_money = check_money(money, choice)

    if change_money >= 0:  
        global water  
        global milk
        global coffee
        
        if "water" in MENU[choice]['ingredients']:
            water -= MENU[choice]['ingredients']['water']
        if "milk" in MENU[choice]['ingredients']:
            milk -= MENU[choice]['ingredients']['milk']
        if "coffee" in MENU[choice]['ingredients']:
            coffee -= MENU[choice]['ingredients']['coffee']

        if change_money > 0:
            print (f"Here is ${ change_money } in change.")
        print(f"Here is your { choice } ☕️. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")

    
def coffee_machine():
    choice_drink = input("  What would you like? (espresso/latte/cappuccino): ").lower()
    
    while power_machine == "on":   
        if (choice_drink == "off"):
            return power_machine == turn_off()
        elif (choice_drink == "report"):
            print(report())
        else:
            is_resources = check_resources(choice_drink)
            if is_resources:
                money = process_coins()
                make_coffee(money, choice_drink)

        choice_drink = input("  What would you like? (espresso/latte/cappuccino): ").lower()

coffee_machine()

