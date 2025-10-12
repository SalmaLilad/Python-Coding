import time

print("Welcome to Saanvi's Pizzaria!")
time.sleep(2)

while True:
    scripts = [
        "\nToday, the pizzas are $10 for a small pizza, $12 for a medium pizza and $15 for a large pizza.",
        "\nThese prices do not include added toppings."
    ]

    for s in scripts:
        print(s)
        try:
            time.sleep(2)
        except KeyboardInterrupt:
            print("The message cannot continue, please pick your pizza.")
            exit()
    break

# Normalize inputs to lowercase for consistency
size = input("What size pizza would you like?\nSmall, Medium, or Large?").lower()
add_pepperoni = input("Would you like to add pepperoni?\nYes or No").lower()
add_peppers = input("Would you like to add some peppers?\nYes or No").lower()
double_cheese = input("Would you like double cheese?\nYes or No").lower()

def pizza_total():
    global total
    total = 0

    if size == "small":
        total += 10
    elif size == "medium":
        total += 12
    elif size == "large":
        total += 15
    else:
        print("Please, select a small, medium, or large pizza")

    if add_pepperoni == "yes":
        if size == "small" or size == "medium":
            total += 2
        else:
            total += 3

    if add_peppers == "yes":
        if size == "small" or size == "medium":
            total += 2
        else:
            total += 3

    if double_cheese == "yes":
        if size == "small" or size == "medium":
            total += 1
        else:
            total += 2

pizza_total()

print(f"Your pizza costs ${total}.")

print('''
            /    \\			
            u  u|      _______
                \\ |  .-''#%&#&%#``-.
            = /  ((%&#&#&%&VK&%&))
                |    `-._#%&##&%_.-'
            /\\/\\`--.   `-."".-'
            |  |    \\   /`./
            |\\/|  \\  `-'  /
            || |   \\     /
            ''')   
