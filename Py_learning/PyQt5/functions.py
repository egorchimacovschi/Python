def happy_birthday(name,age):
    print(f"Happy birthday to {name}, you are {age} years old!")

happy_birthday("Egor",20) 

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount} is due: {due_date}")

display_invoice("Egor", 42.5, "01/01")

def add(num1,num2):
    return num1 + num2

def substract(x,y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x /y

print(add(1,2))
print(substract(1,2))
print(multiply(1,2))
print(divide(1,2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("egor", "chimacovschi")
print(full_name)
