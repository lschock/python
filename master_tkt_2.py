#Treehouse MasterTicket project challenge
#SCRUM User Stories
    # 1)  As a User, I should be shown the number of tickets left remaining, so I can understand the importance of buying now
    # 2)  As a User, I should have a personalized experience so that I feel welcomed by the brand
    # 3)  As a User, I should be able to request a certain amount of tickets and be told the total cost, 
        # so that I can determine if I want to purchase the tickets
    # 4)  As a User, I should be able to confirm my order, so that I do not accidentally purchase more tickets than intended
    # 5)  As a User, I should not be offered tickets if there are not any available
    # 6)  As a User, I should have errors reported in a user friendly manner
    # TODO As a User, I should be able to purchase using credit cards and bitcoin

TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100

def calculate_price(num_of_tickets):
    return (num_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name?  ")
    number_of_tickets = input("Hi {}, how many tickets would you like?  ".format(name))
    try:
        number_of_tickets = int(number_of_tickets)
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue.  {}.  Please try again.".format(err))
    else:
        amount_due = calculate_price(number_of_tickets)
        print("That will be ${}".format(amount_due))
        proceed = input("Would you like to proceed?  Y/N  ")
        if proceed.lower() == "y":
            # TODO:  Gather credit card information and process it
            print("SOLD!")
            tickets_remaining -= number_of_tickets
        else:
            ("Thank you {}.  Have a lovely day!".format(name))
print("Sorry, the tickets are all sold out :(")