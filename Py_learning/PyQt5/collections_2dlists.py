# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

groceries = [["apple", "orange", "banana", "coconut"]\
             ,["celery", "carrots", "potatoes"],\
                ["chicken", "fish", "turkey"]]
#YOU CAN DO THE COLLETIONS OF 2D TUPLES AND SETS TOOO

#print(groceries[0])
#print(groceries[0][0])

for collection in  groceries:
    for food in collection:
        print(food, end=" ")
    print()