employess = ["Eugene", "Sqidward", "Spongebob", "Patrick"]
# import json
# employee = {
    # "name" : "SpongeBob",
    # "age" : 30,
    # "job" : "cook"
# }
file_path = "test"
# 
# import csv
# employees = [["Name", "Age", "Job"],
            #  ["SpongeBob", 30, "cook"],
            #  ["Patrick", 37, "unemplyed"],
            #  ["Sandy", 27, "Scientist"]]

#equals to close at teh end
# r - opens a file for reading
# w - opens a file to write creates a new file or ttruncates the existing one
# a to append th text
# x - creates a nre file ; error if already exists
# b - opens in binary mode
# t - opens in text mode
# + opens for updating reading writiing
try:
    with open(file_path, "w", newline="") as file:
        for employee in employess:
           file.write(employee + '\n')
        print(f"txt file '{file_path}' was created")
        
        # json.dump(employee, file, indent="    ")
        # print("Json at hsi location was craeted")

        # writer = csv.writer(file)
        # for row in employees:
            # writer.writerow(row)
except FileExistsError:
    print("This file already exists")