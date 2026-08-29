import os 
import json
import csv

file_path1 = "test"
file_path2 = "test.csv"
file_path3 = "test.json"

try:
    with open(file_path1, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file is not found")
except PermissionError:
    print("You do not have permisiin to read this file")


try:
    with open(file_path3, "r") as file:
        content = json.load(file)
        print(content["name"])
except FileNotFoundError:
    print("The file is not found")
except PermissionError:
    print("You do not have permisiin to read this file")

try:
    with open(file_path2, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("The file is not found")
except PermissionError:
    print("You do not have permisiin to read this file")
