#!/bin/bash

# Function to display usage instructions
usage() {
    echo "Usage: $0 [source_directory] [backup_directory]"
    exit 1
}

# Check if correct number of arguments is provided
if [ $# -ne 2 ]; then
    usage
fi

SOURCE_DIR=$1
BACKUP_DIR=$2
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Source directory does not exist."
    exit 1
fi

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Create backup
BACKUP_PATH="$BACKUP_DIR/backup_$TIMESTAMP"
mkdir "$BACKUP_PATH"
cp -r "$SOURCE_DIR"/* "$BACKUP_PATH"

echo "Backup of $SOURCE_DIR completed at $BACKUP_PATH"
