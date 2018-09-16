#USER STORIES:
    #As a User, I should be continually prompted so that I can add a grocery item or view my lsit when I need to
    #As a User, I should be able to state when I am DONE, so that I may print out the list in totality
    #As a User, I should be able to ask for HELP so that I can understand how to use the application
    #As a User, I should be able to add an item to the list
    #As a User, upon adding an item to a list, I should know the total length of my list, so that I don't over buy
    #As a User, I should be able to see the list at any time so that I can verify my order

shopping_list = []

def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to show shopping list.
""")


def add_to_list(item):
    shopping_list.append(item)
    print("Item has been added to the list.  There are {} items in the list.".format(len(shopping_list)))


def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)


show_help()
while True:
    new_item = input("> ")
    
    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()    
        continue

    add_to_list(new_item)

show_list()