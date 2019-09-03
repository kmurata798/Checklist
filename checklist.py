print("Hello World")

checklist = list()

# CREATE
def create(item):
    checklist.append(item)
    # Create item code here

# READ
def read(index):
    return checklist[int(index)]
    # Read code here

# UPDATE
def update(index, item):
    checklist[int(index)] = item
    # Update code here

# DESTROY
def destroy(index):
    checklist.pop(int(index))
    # Destroy code here

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    print("[ Item completed √ ]")
    checklist[int(index)] = "√" + checklist[int(index)]
    print(checklist[int(index)])

def unmark_completed(index):
    print("[ Items uncompleted X ]")
    checklist[int(index)] = index + checklist[int(index)]
    print(checklist[int(index)])

def select(function_code):
    # Create item
    if function_code == "C" or function_code == "c":
        input_item = user_input("Input clothing: ")
        create(input_item)
        return True

    # Read item
    elif function_code == "R" or function_code == "r":
        item_index = user_input("Index Number: ")

        # Remember that item_index must actually exist or our program will crash.
        print(item_index + "" + read(item_index))
        return True

    #Update item
    elif function_code == "U" or function_code == "u":
        update_index = user_input("Index you wish to update: ")
        update_item = user_input("Clothing you wish to add: ")
        update(update_index, update_item)
        return True

    elif function_code == "D" or function_code == "d":
        delete = user_input("Index to delete: ")
        destroy(delete)
        return True

    # Print all items
    elif function_code == "P" or function_code == "p":
        list_all_items()
        return True

    elif function_code == "Q" or function_code == "q":
        #this is where we want to stop our loop
        return False

    elif function_code == "M" or function_code == "m":
        mark_input = input("mark off index: ")
        mark_completed(mark_input)
        return True

    elif function_code == "W" or function_code == "w":
        unmark_input = input("Index to unmark: ")
        unmark_completed(unmark_input)
        return True

    # Catch all
    else:
        print("\033[0;31m === Unknown Option === \033[0m")
    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)

    return user_input

def test():

    create("purple sox")
    create("red cloak")
    create("green pants")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    #destroy(1)

    print(read(0))
    print(read(1))

    list_all_items()

    mark_completed(1)
    mark_completed(1)

    unmark_completed(0)

    destroy(0)

    # Your testing code here
    # ...
    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    mark_completed(1)
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run

    user_value = user_input("Please Enter a value:")
    print(user_value)

    

#test()

running = True
while running:
    selection = user_input(
        "Press \033[0;32mC\033[0;0m to add to list, \033[1;35mR\033[0;0m to Read from list, \033[0;34mP\033[0;0m to display list, \033[0;36mM\033[0;0m to checkmark completed, \033[0;33mW\033[0;0m to uncheckmark completed, \033[1;33mU\033[0;0m to update a slot, \033[1;31mD\033[0;0m to delete clothing, and \033[0;31mQ\033[0;0m to quit: ")
    running = select(selection)
