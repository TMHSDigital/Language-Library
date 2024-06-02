import json
import os
import shutil
import logging

logging.basicConfig(filename="config_manager.log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def read_config(file_path):
    with open(file_path, "r") as file:
        config = json.load(file)
    return config

def write_config(file_path, config):
    with open(file_path, "w") as file:
        json.dump(config, file, indent=4)

def backup_config(file_path):
    backup_path = f"{file_path}.bak"
    shutil.copy(file_path, backup_path)
    logging.info(f"Backup created at {backup_path}")

def validate_config(config):
    required_sections = ["server", "database", "logging"]
    for env, settings in config.items():
        for section in required_sections:
            if section not in settings:
                logging.error(f"Missing {section} section in {env} environment")
                return False
    return True

def update_config(file_path, environment, section, key, value):
    config = read_config(file_path)
    if environment in config and section in config[environment]:
        config[environment][section][key] = value
        if validate_config(config):
            backup_config(file_path)
            write_config(file_path, config)
            logging.info(f"Updated {section} - {key}: {value} in {environment} environment")
        else:
            logging.error("Invalid configuration data")
    else:
        logging.error(f"Section {section} not found in {environment} environment")

def display_config(config):
    print(json.dumps(config, indent=4))

if __name__ == "__main__":
    config_file = "config.json"

    while True:
        print("\nConfiguration Management System")
        print("1. Read Configuration")
        print("2. Update Configuration")
        print("3. Display Configuration")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            config = read_config(config_file)
            display_config(config)
        elif choice == "2":
            environment = input("Enter environment to update (development, testing, production): ")
            section = input("Enter section to update (server, database, logging): ")
            key = input("Enter key to update: ")
            value = input("Enter new value: ")
            update_config(config_file, environment, section, key, value)
        elif choice == "3":
            config = read_config(config_file)
            display_config(config)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
