def greet(first, last):
    print(f"Hi there {first} {last}")
    print("Welcome abroad")

greet("egor", "chimacovschi")

def greet_g(name):
    return f"Hi {name}"

print(f"{greet_g("egor")}")
message = greet_g("egor")
file = open ("text.txt", "w")
file.write(message)
file.close

def increment(number, by = 1):
    return number + by
print(increment(5))


def multiply(*numbers):
    print(numbers)

multiply(2, 3, 4, 5)