# banner = list("Congratulations")
# print(banner)

# temperatures = []
# temperatures.append(99.6)
# temperatures.append(98.4)
# print(temperatures)

# er_temp = [101.1, 100.8, 99.9]
# print(er_temp)

# total_temps = temperatures + er_temp
# print(total_temps)

# attendees = ["Ken", "Alena", "Treasure"]
# attendees.append("Ashley")
# attendees.extend(["James", "Guil"])
# optional_invitees = ["Ben J.", "Dave"]
# potential_attendees = attendees + optional_invitees
# print("There are", len(potential_attendees), "potential attendees currently.")

# books = [
#     "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
#     "Python for Data Analysis - Wes McKinney",
#     "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
#     "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
#     "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
# ]

# video_games = [
#     "The Legend of Zelda: Breath of the Wild",
#     "Splatoon 2",
#     "Super Mario Odyssey",
# ]
# print("Suggested gift: {}".format(books[0]))

# print("Books:")
# for book in books:
#     print("* " + book)

# def display_wishlist(display_name, wishes):
#     items = wishes.copy()
#     print(display_name + ":")
#     suggested_gift = items.pop(0)
#     print("=====>", suggested_gift, "<=====")
#     for item in items:
#         print("* " + item)
#     print()

# display_wishlist("Books", books)
# display_wishlist("Video Games", video_games)


#insert at beginning of list

# books.insert(0, "Learning Python: Powerful Object-Oriented Programming - Mark Lutz")
# print(books)

# lauries_taco = "\N{TACO}"
# print(lauries_taco)



# continents = [
#     'Asia',
#     'South America',
#     'North America',
#     'Africa',
#     'Europe',
#     'Antarctica',
#     'Australia',
# ]
# # Your code here
# for continent in continents:
#     if continent[0] == "A":
#     	print("* " + continent)


# inventory = ["shield", "apple", "sword", "bow", "boomerang"]
# for item in inventory.copy():
#     inventory.remove(item)


turtles = [
    "Michelangelo",
    "Leonardo",
    "Raphael",
    "Donatello",
]

def shredder(names):
    if len(names) >= 1:
        names[0] = "Bebop"

shredder(turtles)

for turtle in turtles:
    print("* " + turtle)