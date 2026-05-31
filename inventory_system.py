# =========================
# MINI PROJECT 5
# Inventory Management System
# =========================

FILE_NAME = "inventory.txt"


class Item:

    def __init__(self, item_id, name, quantity):

        self.item_id = item_id
        self.name = name
        self.quantity = quantity

    def to_file_format(self):

        return f"{self.item_id},{self.name},{self.quantity}\n"


# -------------------------
# ADD ITEM
# -------------------------
def add_item():

    item_id = input("Item ID: ")
    name = input("Item Name: ")
    quantity = int(input("Quantity: "))

    item = Item(item_id, name, quantity)

    with open(FILE_NAME, "a") as file:

        file.write(item.to_file_format())

    print("Item added successfully")


# -------------------------
# VIEW ITEMS
# -------------------------
def view_items():

    try:

        with open(FILE_NAME, "r") as file:

            items = file.readlines()

            if not items:

                print("No inventory records")

                return

            print("\nInventory List")

            for item in items:

                item_id, name, quantity = item.strip().split(",")

                print(
                    f"ID: {item_id} | Name: {name} | Qty: {quantity}"
                )

    except FileNotFoundError:

        print("Inventory file not found")


# -------------------------
# SEARCH ITEM
# -------------------------
def search_item():

    search_id = input("Enter Item ID: ")

    found = False

    try:

        with open(FILE_NAME, "r") as file:

            for item in file:

                item_id, name, quantity = item.strip().split(",")

                if item_id == search_id:

                    print(
                        f"Found -> {name} ({quantity})"
                    )

                    found = True

                    break

        if not found:

            print("Item not found")

    except FileNotFoundError:

        print("Inventory file not found")


# -------------------------
# UPDATE STOCK
# -------------------------
def update_stock():

    update_id = input("Enter Item ID: ")

    updated_items = []

    found = False

    try:

        with open(FILE_NAME, "r") as file:

            items = file.readlines()

        for item in items:

            item_id, name, quantity = item.strip().split(",")

            if item_id == update_id:

                new_quantity = input(
                    "Enter new quantity: "
                )

                updated_items.append(
                    f"{item_id},{name},{new_quantity}\n"
                )

                found = True

            else:

                updated_items.append(item)

        with open(FILE_NAME, "w") as file:

            file.writelines(updated_items)

        if found:

            print("Stock updated successfully")

        else:

            print("Item not found")

    except FileNotFoundError:

        print("Inventory file not found")


# -------------------------
# DELETE ITEM
# -------------------------
def delete_item():

    delete_id = input("Enter Item ID: ")

    updated_items = []

    found = False

    try:

        with open(FILE_NAME, "r") as file:

            items = file.readlines()

        for item in items:

            item_id, name, quantity = item.strip().split(",")

            if item_id != delete_id:

                updated_items.append(item)

            else:

                found = True

        with open(FILE_NAME, "w") as file:

            file.writelines(updated_items)

        if found:

            print("Item deleted successfully")

        else:

            print("Item not found")

    except FileNotFoundError:

        print("Inventory file not found")


# -------------------------
# MENU
# -------------------------
def show_menu():

    print("\n===== INVENTORY SYSTEM =====")

    print("1. Add Item")
    print("2. View Items")
    print("3. Search Item")
    print("4. Update Stock")
    print("5. Delete Item")
    print("6. Exit")


# -------------------------
# MAIN LOOP
# -------------------------
while True:

    show_menu()

    choice = input("Enter choice: ")

    if choice == "1":

        add_item()

    elif choice == "2":

        view_items()

    elif choice == "3":

        search_item()

    elif choice == "4":

        update_stock()

    elif choice == "5":

        delete_item()

    elif choice == "6":

        print("Exiting Inventory System")

        break

    else:

        print("Invalid choice")
        
        
        