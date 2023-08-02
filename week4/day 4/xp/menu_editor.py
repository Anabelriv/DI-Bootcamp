from menu_item import MenuItem
from menu_manager import MenuManager


def show_user_menu():
    while True:
        print("\n--- Program Menu ---")
        print("V: View an Item")
        print("A: Add an Item")
        print("D: Delete an Item")
        print("U: Update an Item")
        print("S: Show the Menu")
        print("E: Exit Program")

        user_input = input("Enter your choice: ").upper()

        if user_input == "V":
            view_item()
        elif user_input == "A":
            add_item_to_menu()
        elif user_input == "D":
            delete_item()
        elif user_input == "U":
            update_item()
        elif user_input == "S":
            show_restaurant_menu()
        elif user_input == "E":
            show_restaurant_menu()
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please try again.")


def view_item():
    name = input("Enter the item's name you want to view: ")
    item = MenuManager.get_by_name(name)
    if item:
        print(f"Name: {item.name}, Price: {item.price}")
    else:
        print("Item not found.")


def add_item_to_menu():
    name = input("Enter the item's name: ")
    price = float(input("Enter the item's price: "))
    item = MenuItem(name, price)
    item.save()
    print("Item was added successfully.")


def delete_item():
    name = input("Enter the name of the item to delete: ")
    item = MenuManager.get_by_name(name)
    if item:
        item.delete()
        print("Item was deleted successfully.")
    else:
        print("Item not found.")


def update_item():
    name = input("Enter the name of the item to update: ")
    item = MenuManager.get_by_name(name)
    if item:
        new_name = input("Enter the new name for the item: ")
        new_price = float(input("Enter the new price for the item: "))
        item.update(new_name, new_price)
        print("Item was updated successfully.")
    else:
        print("Item not found.")


def show_restaurant_menu():
    items = MenuManager.all_items()
    print("\n--- Restaurant Menu ---")
    for item in items:
        print(f"Name: {item.name}, Price: {item.price}")


if __name__ == "__main__":
    show_user_menu()
