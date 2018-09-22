#USER STORIES:
    #As a User, I should be continually prompted so that I can add a grocery item or view my lsit when I need to
    #As a User, I should be able to state when I am DONE, so that I may print out the list in totality
    #As a User, I should be able to ask for HELP so that I can understand how to use the application
    #As a User, I should be able to add an item to the list
    #As a User, upon adding an item to a list, I should know the total length of my list, so that I don't over buy
    #As a User, I should be able to see the list at any time so that I can verify my order
import os
shopping_list = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_help():
    clear_screen()
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to show shopping list.
Enter 'REMOVE' to remove an item from list.
""")


def add_to_list(item):
    show_list()
    if len(shopping_list):
        position = input("Where should I add {}?\n"
                        "Press ENTER to add to the end of the list\n"
                        "> ".format(item))
    else:
        position = 0
    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(new_item)
    show_list()

    
def show_list():
    clear_screen()
    print("Here's your list:")

    for index, item in enumerate(shopping_list, start=1):
        print("{}. {}".format(index, item))
        print("-" * 10)
        
        
def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove?\n  ")
    try:
        shopping_list.remove(what_to_remove)
    except:
        pass
    show_list()

show_help()
while True:
    new_item = input("> ")
    
    if new_item.upper() == "DONE" or new_item.upper() == "QUIT":
        break
    elif new_item.upper() == "HELP":
        show_help()
        continue
    elif new_item.upper() == "SHOW":
        show_list()    
        continue
    elif new_item.upper() == "REMOVE":
        remove_from_list()
    add_to_list(new_item)

show_list()