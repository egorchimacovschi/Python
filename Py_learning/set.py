#Set = {} unordered and immutable, but Add/.Remove OK, No duplicates

fruits = {"apple", "orange", "banana", "coconut"}
print(fruits)
print(len(fruits))
print("apple" in fruits)

fruits.add("popcorn")
print(fruits)

fruits.remove("popcorn")
print(fruits)

fruits.pop()
print(fruits)

# fruits.clear()