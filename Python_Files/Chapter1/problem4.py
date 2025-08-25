import os

# specify the directry path that you want to repesent:
directory_path = '/Windows'  # Replace with your target directory

try:
    # List of all entries in the directory according to your path:
    entries = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    # print all the entries(directories/files) in directory that's path is given:
    print(entries)
    print(f"Contents of '{directory_path}' as a format(item):")
    for item in entries:
    # print the all the directories/files as a format(item) in the target directory that you want display:
        print(item)
    # Except these directories/files that's path are not exit or those files/directories that denies the permission of access:
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
