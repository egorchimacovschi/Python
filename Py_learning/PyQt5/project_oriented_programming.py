#object = abundle of related atrbutes (variables) and methods (functions)
# you need to create class to create objects
# class = used to design the structure and layout of an object
from my_class import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)

print(car1.year)
print(car1.model)
print(car1.for_sale)
print(car1.color)

print(car2.year)
print(car2.model)
print(car2.for_sale)
print(car2.color)

car1.drive()
car2.stop()