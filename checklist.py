print("Hello World")

checklist = list()

# CREATE
def create(item):
    checklist.append(item)
    # Create item code here

# READ
def read(index):
    return checklist[index]
    # Read code here

# UPDATE
def update(index, item):
    checklist[index] = item
    # Update code here

# DESTROY
def destroy(index):
    checklist.pop(index)
    # Destroy code here

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    print("[ Items completed √ ]")
    checklist[index] = '√' + checklist[index]
    print(checklist[index])

def select(function_code):
    # Create item
    if function_code == "c":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "r":
        item_index = user_input("Index Number?")

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    #Update item
    elif function_code == "u":
        update()

    # Print all items
    elif function_code == "p":
        list_all_items()

    elif function_code == "q":
        #this is where we want to stop our loop
        return False

    # Catch all
    else:
        print("Unknown Option")
    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def test():

    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    #destroy(1)

    print(read(0))
    print(read(1))

    list_all_items()

    mark_completed(1)

    # Your testing code here
    # ...
    # Call your new function with the appropriate value
    select("c")
    # View the results
    list_all_items()
    # Call function with new value
    select("r")
    # View results
    list_all_items()
    # Continue until all code is run

    user_value = user_input("Please Enter a value:")
    print(user_value)

#test()

running = True
while running:
    #str.casefold("blabla") --> unrestricts case sensitivity
    selection = str.casefold(user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit: "))
    running = select(selection)
