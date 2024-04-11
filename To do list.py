# Define an empty list to store the to-do items
todo_list = []

# Function to add an item to the to-do list
def add_item(item):
    todo_list.append(item)
    print("Item added to the to-do list.")

# Function to remove an item from the to-do list
def remove_item(item):
    if item in todo_list:
        todo_list.remove(item)
        print("Item removed from the to-do list.")
    else:
        print("Item not found in the to-do list.")

# Function to display the current to-do list
def display_list():
    print("To-Do List:")
    for index, item in enumerate(todo_list, start=1):
        print(f"{index}. {item}")

# Main loop
while True:
    print("\nChoose an option:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Display list")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        item = input("Enter the item to add: ")
        add_item(item)
    elif choice == "2":
        item = input("Enter the item to remove: ")
        remove_item(item)
    elif choice == "3":
        display_list()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
