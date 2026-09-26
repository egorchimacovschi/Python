while   True:
    principle = float(input("Enter another principle :"))
    if principle < 0 :
        print("Principle can't be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter another principle :"))
    if rate < 0 :
        print("Principle can't be less than or equal to zero")
    else:
        break

while True:
    time = int(input("Enter another principle :"))
    if time < 0 :
        print("Principle can't be less than or equal to zero")
    else:
        break

interest = principle * pow((1+ rate / 100), time)

print(f"Balance wiil be {interest:.2f}")