#DICTIONARY = a collections of {key:value} \
# pairs ordered and changable.No duplicates

capitals = {"USA":"Washingoton D.C",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

# print(dir(capitals))
# print(help(capitals))

print(capitals.get("USA"))
print(capitals.get("Japan")) #none

if not capitals.get("Japan"):
    print("NOT")

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Detroit"})
capitals.pop("China")
capitals.popitem() #remove last item
#capitals.clear()
print(capitals)

keys = capitals.keys()
print(keys)

for key in keys:
    print(key)


values = capitals.values()

for value in values:
    print(value)

items = capitals.items()

print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")