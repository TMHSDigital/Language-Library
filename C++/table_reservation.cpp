#include <iostream>
#include <vector>
#include <string>

class Reservation {
public:
    Reservation(int tableNumber, std::string customerName, std::string time)
        : tableNumber(tableNumber), customerName(customerName), time(time) {}
    int getTableNumber() { return tableNumber; }
    std::string getCustomerName() { return customerName; }
    std::string getTime() { return time; }

private:
    int tableNumber;
    std::string customerName;
    std::string time;
};

class TableReservationSystem {
public:
    void addReservation(int tableNumber, std::string customerName, std::string time) {
        reservations.push_back(Reservation(tableNumber, customerName, time));
    }

    void viewReservations() {
        if (reservations.empty()) {
            std::cout << "No reservations to display.\n";
            return;
        }
        for (auto& reservation : reservations) {
            std::cout << "Table Number: " << reservation.getTableNumber()
                      << ", Customer Name: " << reservation.getCustomerName()
                      << ", Time: " << reservation.getTime() << "\n";
        }
    }

    void cancelReservation(int tableNumber) {
        for (auto it = reservations.begin(); it != reservations.end(); ++it) {
            if (it->getTableNumber() == tableNumber) {
                reservations.erase(it);
                std::cout << "Reservation for table number " << tableNumber << " cancelled.\n";
                return;
            }
        }
        std::cout << "No reservation found for table number " << tableNumber << ".\n";
    }

private:
    std::vector<Reservation> reservations;
};

int main() {
    TableReservationSystem trs;
    int choice, tableNumber;
    std::string customerName, time;

    while (true) {
        std::cout << "\nTable Reservation System:\n";
        std::cout << "1. Add Reservation\n";
        std::cout << "2. View Reservations\n";
        std::cout << "3. Cancel Reservation\n";
        std::cout << "4. Exit\n";
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                std::cout << "Enter Table Number: ";
                std::cin >> tableNumber;
                std::cout << "Enter Customer Name: ";
                std::cin.ignore();
                std::getline(std::cin, customerName);
                std::cout << "Enter Time (HH:MM): ";
                std::getline(std::cin, time);
                trs.addReservation(tableNumber, customerName, time);
                break;
            case 2:
                trs.viewReservations();
                break;
            case 3:
                std::cout << "Enter Table Number to cancel: ";
                std::cin >> tableNumber;
                trs.cancelReservation(tableNumber);
                break;
            case 4:
                std::cout << "Exiting...\n";
                return 0;
            default:
                std::cout << "Invalid choice. Please try again.\n";
        }
    }
}
