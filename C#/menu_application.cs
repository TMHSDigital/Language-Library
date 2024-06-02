using System;
using System.Collections.Generic;

class MenuItem
{
    public string Name { get; set; }
    public double Price { get; set; }

    public MenuItem(string name, double price)
    {
        Name = name;
        Price = price;
    }

    public void Display()
    {
        Console.WriteLine($"Name: {Name}, Price: ${Price}");
    }
}

class Menu
{
    private List<MenuItem> items = new List<MenuItem>();

    public void AddItem(string name, double price)
    {
        items.Add(new MenuItem(name, price));
    }

    public void ViewItems()
    {
        if (items.Count == 0)
        {
            Console.WriteLine("No items to display.");
            return;
        }
        foreach (var item in items)
        {
            item.Display();
        }
    }

    public void RemoveItem(string name)
    {
        items.RemoveAll(item => item.Name == name);
    }
}

class Program
{
    static void Main()
    {
        Menu menu = new Menu();
        int choice;
        string name;
        double price;

        while (true)
        {
            Console.WriteLine("\nRestaurant Menu Application:");
            Console.WriteLine("1. Add Menu Item");
            Console.WriteLine("2. View Menu Items");
            Console.WriteLine("3. Remove Menu Item");
            Console.WriteLine("4. Exit");
            Console.Write("Enter your choice: ");
            choice = int.Parse(Console.ReadLine());

            switch (choice)
            {
                case 1:
                    Console.Write("Enter item name: ");
                    name = Console.ReadLine();
                    Console.Write("Enter item price: ");
                    price = double.Parse(Console.ReadLine());
                    menu.AddItem(name, price);
                    break;
                case 2:
                    menu.ViewItems();
                    break;
                case 3:
                    Console.Write("Enter item name to remove: ");
                    name = Console.ReadLine();
                    menu.RemoveItem(name);
                    break;
                case 4:
                    Console.WriteLine("Exiting...");
                    return;
                default:
                    Console.WriteLine("Invalid choice. Please try again.");
                    break;
            }
        }
    }
}
