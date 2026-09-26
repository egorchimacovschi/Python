name = input ("Enter your name ")

while name == "":
    print("Error")
    name = input ("Enter your name")

print(f"Hello {name}")


food = input ("Enter you favourite food ")

while not food == "q":
    print(f"You Like {food}")
    food = input ("Entered you favourite food ")

print ("bye")


num = int(input ("Enter a number between 1- 10: "))

while num < 1 or num >10 :
    print(f"{num} is not valid")
    num = int(input ("Enter anothe rnumber "))

print(f"Your number is {num}")