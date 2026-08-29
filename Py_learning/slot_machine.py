import random

def spin_row():
    symbols = ['1', '2', '3', '4', '5']

    return [random.choice(symbols) for _ in range (3)]

def print_row(row):
    print(" ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '1':
            return bet * 3
        elif row[0] == '2':
            return bet * 4
        elif row[0] == '3':
            return bet * 5
        elif row[0] == '4':
            return bet * 10
        elif row[0] == '5':
            return bet * 20
    return 0

def main():
    balance = 100

    print("Welcome to python slots")
    print("Symbols: 1 2 3 4 5")

    while balance > 0:
        print(f"Current balamce is ${balance}")

        bet = input("Place youre bet amount: ")
        if not bet.isdigit():
            print("Please enter a valid number")
            continue
        bet = int(bet)

        if bet > balance:
            print("Insuficent balance")
            continue
        if bet <= 0:
            print("That must be greater than 0")
            continue

        balance -= bet
        row = spin_row()
        print("Spining...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Yo lost this round")

        balance += payout

        play_again = input("Do you want to play again? (Y/N)").upper()

        if play_again != 'Y':
            break
    print(f"Game is over youre balance is ${balance}")

if __name__ == '__main__':
    main()