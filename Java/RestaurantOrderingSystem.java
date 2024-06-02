import java.util.ArrayList;
import java.util.Scanner;

class MenuItem {
    String name;
    double price;

    MenuItem(String name, double price) {
        this.name = name;
        this.price = price;
    }
}

class Order {
    ArrayList<MenuItem> items = new ArrayList<>();
    void addItem(MenuItem item) {
        items.add(item);
    }
    void displayOrder() {
        double total = 0;
        System.out.println("Order:");
        for (MenuItem item : items) {
            System.out.println(item.name + " - $" + item.price);
            total += item.price;
        }
        System.out.println("Total: $" + total);
    }
}

public class RestaurantOrderingSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<MenuItem> menu = new ArrayList<>();
        Order order = new Order();

        menu.add(new MenuItem("Burger", 8.99));
        menu.add(new MenuItem("Fries", 3.49));
        menu.add(new MenuItem("Soda", 1.99));
        menu.add(new MenuItem("Salad", 4.99));

        while (true) {
            System.out.println("\nRestaurant Ordering System:");
            System.out.println("1. View Menu");
            System.out.println("2. Place Order");
            System.out.println("3. Display Bill");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("Menu:");
                    for (MenuItem item : menu) {
                        System.out.println(item.name + " - $" + item.price);
                    }
                    break;
                case 2:
                    System.out.println("Enter the name of the item to order:");
                    scanner.nextLine();
                    String itemName = scanner.nextLine();
                    boolean found = false;
                    for (MenuItem item : menu) {
                        if (item.name.equalsIgnoreCase(itemName)) {
                            order.addItem(item);
                            System.out.println(item.name + " added to order.");
                            found = true;
                            break;
                        }
                    }
                    if (!found) {
                        System.out.println("Item not found in menu.");
                    }
                    break;
                case 3:
                    order.displayOrder();
                    break;
                case 4:
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}
