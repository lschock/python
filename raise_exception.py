    #CHECK PLEASE - watch for exception activity
# import math

# def split_check(total, number_of_people):
#     if number_of_people <= 1:
#         raise ValueError("More than 1 person is required to split the check")
#     return math.ceil(total / number_of_people)

# try:
#     total_due = float(input("What is the total?  "))
#     number_of_people = int(input("How many people?  "))
#     amount_due = split_check(total_due, number_of_people)

# except ValueError as err:
#     print("Please enter a valid value!")
#     print("({})".format(err))
# else: 
#     print("Each person owes ${}".format(amount_due))

#----------------------------------------------------------------------------------------#

# I've made a function that creates brand new product names using "artificial intelligence".
# I have a problem though, people keep on adding product ideas that are too short. It makes the suggestions look bad.
# Can you please raise a ValueError if the product_idea is less than 3 characters long? product_idea is a string. Thanks in advance!


def suggest(product_idea):
    if len(product_idea) < 3:
        raise ValueError("Please enter a minimum of 3 characters.")
    return product_idea + "inator"

