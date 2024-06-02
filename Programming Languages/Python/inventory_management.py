import json

class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class InventoryManagementSystem:
    def __init__(self):
        self.inventory = []

    def add_item(self, name, quantity, price):
        self.inventory.append(Item(name, quantity, price))

    def view_items(self):
        if not self.inventory:
            print("No items in inventory.")
            return
        for item in self.inventory:
            print(f"Name: {item.name}, Quantity: {item.quantity}, Price: ${item.price:.2f}")

    def update_item(self, name, quantity, price):
        for item in self.inventory:
            if item.name == name:
                item.quantity = quantity
                item.price = price
                print(f"Item {name} updated.")
                return
        print(f"Item {name} not found in inventory.")

    def delete_item(self, name):
        self.inventory = [item for item in self.inventory if item.name != name]
        print(f"Item {name} deleted.")

def main():
    ims = InventoryManagementSystem()
    while True:
        print("\nInventory Management System:")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            ims.add_item(name, quantity, price)
        elif choice == "2":
            ims.view_items()
        elif choice == "3":
            name = input("Enter item name to update: ")
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            ims.update_item(name, quantity, price)
        elif choice == "4":
            name = input("Enter item name to delete: ")
            ims.delete_item(name)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
