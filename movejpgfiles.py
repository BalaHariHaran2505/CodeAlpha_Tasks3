"""
Python Script: Move all .jpg files from one folder to another
Author: Your Name
Date: 2025-08-16
"""

import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    """
    Moves all .jpg files from source_folder to destination_folder.
    """
    # Create destination folder if it does not exist
    os.makedirs(destination_folder, exist_ok=True)

    # Track moved files
    moved_files = []

    # Loop through files in source folder
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.jpg'):  # case-insensitive
            src_path = os.path.join(source_folder, filename)
            dst_path = os.path.join(destination_folder, filename)
            shutil.move(src_path, dst_path)
            moved_files.append(filename)
            print(f"Moved: {filename}")

    print(f"\nTotal {len(moved_files)} .jpg files moved successfully!")

if __name__ == "__main__":
    source = input("Enter the path of the source folder: ")
    destination = input("Enter the path of the destination folder: ")
    move_jpg_files(source, destination)
