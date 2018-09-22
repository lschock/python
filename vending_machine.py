
sodas = ["Pepsi", "Cherry Coke Zero", "Sprite"]
chips = ["Doritos", "Fritos"]
candy = ["Snickers", "M&Ms", "Twizzlers"]

while True:
    choice = input("Would you like a SODA, CHIPS, or CANDY?  ").lower()
    if choice == 'soda':
        snack = sodas.pop()
    elif choice == 'chips':
        snack = chips.pop()
    elif choice == 'candy':
        snack = candy.pop()
    else:
        print("Sorry, I didn't understand that.")
        continue
    print("Here's your {}:  {}".format(choice, snack))