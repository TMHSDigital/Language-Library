package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
    "strings"
)

type Item struct {
    Name  string
    Price float64
    Stock int
}

var inventory []Item

func addItem(name string, price float64, stock int) {
    inventory = append(inventory, Item{Name: name, Price: price, Stock: stock})
}

func viewItems() {
    if len(inventory) == 0 {
        fmt.Println("No items to display.")
        return
    }
    for _, item := range inventory {
        fmt.Printf("Name: %s, Price: $%.2f, Stock: %d\n", item.Name, item.Price, item.Stock)
    }
}

func deleteItem(name string) {
    for i, item := range inventory {
        if item.Name == name {
            inventory = append(inventory[:i], inventory[i+1:]...)
            fmt.Printf("Item %s deleted.\n", name)
            return
        }
    }
    fmt.Printf("Item %s not found.\n", name)
}

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    for {
        fmt.Println("\nInventory Management System:")
        fmt.Println("1. Add Item")
        fmt.Println("2. View Items")
        fmt.Println("3. Delete Item")
        fmt.Println("4. Exit")
        fmt.Print("Enter your choice: ")
        scanner.Scan()
        choice, _ := strconv.Atoi(scanner.Text())

        switch choice {
        case 1:
            fmt.Print("Enter item name: ")
            scanner.Scan()
            name := scanner.Text()
            fmt.Print("Enter item price: ")
            scanner.Scan()
            price, _ := strconv.ParseFloat(scanner.Text(), 64)
            fmt.Print("Enter item stock: ")
            scanner.Scan()
            stock, _ := strconv.Atoi(scanner.Text())
            addItem(name, price, stock)
        case 2:
            viewItems()
        case 3:
            fmt.Print("Enter item name to delete: ")
            scanner.Scan()
            name := scanner.Text()
            deleteItem(name)
        case 4:
            fmt.Println("Exiting...")
            return
        default:
            fmt.Println("Invalid choice. Please try again.")
        }
    }
}
