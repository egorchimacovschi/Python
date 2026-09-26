fruits = ["apple", "orange", "banana", "coconut"]
#LIsts = [] ordered and changabele. Duplicates are OK.


# print(fruits)
# print(fruits[0])
# print(fruits[:3])
# print(fruits[::2])
# print(fruits[::-1])

# for fruit in fruits:
    # print(fruit)

# print(dir(fruits))
# print(help(fruits))

# print(len(fruits))

# print("apple" in fruits) #reeturns TRue

fruits[0] = "pineapple"
fruits.append("apple")
fruits.remove("pineapple")
fruits.insert(0, "popcron")
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

# fruits.clear()
# print(fruits)

print(fruits.index("apple"))
print(fruits.count("apple"))