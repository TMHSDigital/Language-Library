import json

class Order:
    def __init__(self, table_number, items):
        self.table_number = table_number
        self.items = items

class OrderManagementSystem:
    def __init__(self):
        self.orders = []

    def add_order(self, table_number, items):
        self.orders.append(Order(table_number, items))

    def view_orders(self):
        if not self.orders:
            print("No orders to display.")
            return
        for order in self.orders:
            print(f"Table Number: {order.table_number}, Items: {', '.join(order.items)}")

    def delete_order(self, table_number):
        self.orders = [order for order in self.orders if order.table_number != table_number]

def main():
    oms = OrderManagementSystem()
    while True:
        print("\nRestaurant Order Management System:")
        print("1. Add Order")
        print("2. View Orders")
        print("3. Delete Order")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            table_number = input("Enter table number: ")
            items = input("Enter items (comma separated): ").split(", ")
            oms.add_order(table_number, items)
        elif choice == "2":
            oms.view_orders()
        elif choice == "3":
            table_number = input("Enter table number to delete: ")
            oms.delete_order(table_number)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
