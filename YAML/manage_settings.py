import yaml
import os
import shutil

CONFIG_FILE = "D:/CODING/Programming Languages/YAML/settings.yaml"
BACKUP_FILE = CONFIG_FILE + ".bak"

def read_config():
    with open(CONFIG_FILE, "r") as file:
        return yaml.safe_load(file)

def write_config(config):
    with open(CONFIG_FILE, "w") as file:
        yaml.safe_dump(config, file)

def backup_config():
    shutil.copy(CONFIG_FILE, BACKUP_FILE)

def update_config(environment, section, key, value):
    config = read_config()
    if environment in config and section in config[environment]:
        config[environment][section][key] = value
        backup_config()
        write_config(config)
    else:
        print(f"Section {section} not found in {environment} environment.")

def display_config(config):
    print(yaml.dump(config, default_flow_style=False))

if __name__ == "__main__":
    while True:
        print("\nSettings Management System")
        print("1. Read Settings")
        print("2. Update Settings")
        print("3. Display Settings")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            config = read_config()
            display_config(config)
        elif choice == "2":
            environment = input("Enter environment to update (development, testing, production): ")
            section = input("Enter section to update (server, database, logging): ")
            key = input("Enter key to update: ")
            value = input("Enter new value: ")
            update_config(environment, section, key, value)
        elif choice == "3":
            config = read_config()
            display_config(config)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
