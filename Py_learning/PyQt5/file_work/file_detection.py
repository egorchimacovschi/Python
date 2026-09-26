import os

file_path = "your path"
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That's a file")
    if os.path.isdir(file_path):
        print("That's the directory")
else:
    print("This location doesnt exists")
