# import time

# quote = "The greatest teacher failure is"
# words = quote.split()

# for word in words:
#     print(words)
#     time.sleep(.5)

#.join() belongs to strings
    
attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Guil"])
optional_invitees = ["Ben J.", "Dave"]
potential_attendees = attendees + optional_invitees
print("There are", len(potential_attendees), "potential attendees currently.")

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invitees)
print("To: " + to_line)
print("CC: " + cc_line)

to_line.split(", ")
print(to_line.split(", "))