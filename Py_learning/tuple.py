#Tuple = () ordered and unchangable. Duplicates OK, Faster

fruits = ("apple", "orange", "banana", "coconut")
print(len(fruits))
print("apple" in fruits)

print(fruits.index("apple"))
print(fruits.count("coconut"))

for fruit in fruits:
    print(fruit, end= " ")
print("")