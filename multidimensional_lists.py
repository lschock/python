travel_expenses = [
    [5.00, 2.75, 22.00, 0.00, 0.00],
    [24.75, 5.50, 15.00, 22.00, 8.00],
    [2.75, 5.50, 0.00, 29.00, 5.00],
]

print("Travel Expenses:")
week_number = 1
for week in travel_expenses:
    print("* Week # {}: ${}".format(week_number, sum(week)))
    week_number += 1
    
# Challenge Task 1 of 2
# Here is a multi-dimensional list of musical groups. The first dimension is group, the second is group members.
# Can you loop through each group and output the members joined together with a ", " comma space as a separator, please?

# Now I'd like to see only groups that are trios, you know 3 members.
# So can you please only print out the trios? It should still use the joined string format from task 1.

musical_groups = [
    ["Ad Rock", "MCA", "Mike D."],
    ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"],
    ["Salt", "Peppa", "Spinderella"],
    ["Rivers Cuomo", "Patrick Wilson", "Brian Bell", "Scott Shriner"],
    ["Chuck D.", "Flavor Flav", "Professor Griff", "Khari Winn", "DJ Lord"],
    ["Axl Rose", "Slash", "Duff McKagan", "Steven Adler"],
    ["Run", "DMC", "Jam Master Jay"],
]
for member in musical_groups:
    if len(member) == 3:
        print(", ".join(member))


