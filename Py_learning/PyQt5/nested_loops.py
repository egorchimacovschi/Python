rows = int(input("Ente rthe amount of raws: "))
columns = int(input("Enter the amount of columns: "))
symbol = input ("Enter a symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()