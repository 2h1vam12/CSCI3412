#!/usr/bin/python3 

import os
import sys

#callback function to accumulate file sizes 
def accumulate_size(file_size, total_size):
    total_size[0] += file_size

# recursively search for files and calculate total size
def find_files(directory, filename, callback, total_size):
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                # not a directory, symlink, socket, etc.
                if entry.is_file() and not entry.is_symlink():
                    if filename in entry.name:
                        file_size = os.stat(entry.path).st_size
                        print(f"{entry.path} {file_size} bytes")
                        callback(file_size, total_size)
                
                # entry is a directory, recursively search inside
                elif entry.is_dir():
                    find_files(entry.path, filename, callback, total_size)

    except PermissionError:
        pass  # skip directories w/o permission to access
    except FileNotFoundError:
        pass  # Handle cases where a directory disappears while traversing

# Main function to handle input and execute the search
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: myFind.py <starting-directory> <filename>")
        sys.exit(1)

    start_dir = sys.argv[1]
    file_name = sys.argv[2]

    print(f"# myFind {start_dir} {file_name}\n")

    # list to store total_size so it can be modified inside recursion
    total_size = [0]

    # initalize recursive search
    find_files(start_dir, file_name, accumulate_size, total_size)

    # Print total size of found files
    print(f"\nTotal files size: {total_size[0]} bytes")



