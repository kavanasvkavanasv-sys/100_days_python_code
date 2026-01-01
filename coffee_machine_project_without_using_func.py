MENU = {
    "report": {
        "ingredients": {
            "water": 100,
            "coffee": 100,
            "milk": 50,
        },
        "cost": 2.5,
    },
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
user_choice = input("What would you like? (espresso/latte/cappuccino)")
machine_off = False
while not machine_off:
    if user_choice == "report":
        print(f"water: {MENU[user_choice]["ingredients"] ["water"]}ml \nMilk:{MENU[user_choice]["ingredients"] ["milk"]}ml\ncoffee:{MENU[user_choice]["ingredients"] ["coffee"]}g  \nMoney : ${MENU[user_choice]["cost"]}")
    elif user_choice == "off":
        machine_off = True
        break
    if (MENU[user_choice]["ingredients"]["water"] < MENU["report"]["ingredients"] ["water"]) and (MENU[user_choice]["ingredients"]["coffee"] < MENU["report"]["ingredients"] ["coffee"]) and (MENU[user_choice]["ingredients"]["milk"] < MENU["report"]["ingredients"] ["milk"]):
        print("please insert coins 'quarters' = $0.25, 'dimes' = $0.10, 'nickles' = $0.05, 'pennies' = $0.01")
        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickles = int(input("How many nickles?"))
        pennies = int(input("How many pennies?"))
        total_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
        total_money = round(total_money, 2)
        print(f"here is  ${total_money} in change")

        if (MENU[user_choice]["cost"]) > total_money:
            print("not enough money")
        else:
            change = total_money - MENU[user_choice]["cost"]
            MENU["report"]["cost"] += total_money
            MENU["report"]["cost"] -= change
            print(f"here is  ${MENU[user_choice]['cost']} money in machine")
            print("report before purchasing")
            print(f"water: {MENU["report"]["ingredients"]["water"]}ml \nMilk:{MENU["report"]["ingredients"]["milk"]}ml\ncoffee:{MENU["report"]["ingredients"]["coffee"]}g  \nMoney : ${MENU["report"]["cost"]}")
            MENU["report"]["ingredients"]["water"] -= MENU[user_choice]["ingredients"]["water"]
            MENU["report"]["ingredients"]["milk"] -= MENU[user_choice]["ingredients"]["milk"]
            MENU["report"]["ingredients"]["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
            MENU[user_choice]['cost'] -= MENU[user_choice]['cost']
            print("report after purchasing")
            print(f"water: {MENU["report"]["ingredients"]["water"]}ml \nMilk:{MENU["report"]["ingredients"]["milk"]}ml\ncoffee:{MENU["report"]["ingredients"]["coffee"]}g  \nMoney : ${MENU["report"]["cost"]}")
            print(MENU)
            print(f"here is your ☕☕{user_choice} ☕☕enjoy")
    elif (MENU[user_choice]["ingredients"]["water"] > MENU["report"]["ingredients"] ["water"]):
        print("sorry not enough water")
    elif (MENU[user_choice]["ingredients"]["milk"] > MENU["report"]["ingredients"] ["milk"]):
        print("sorry not enough milk")
    elif (MENU[user_choice]["ingredients"]["coffee"] > MENU["report"]["ingredients"] ["coffee"]):
        print("sorry not enough coffee")





