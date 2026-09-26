price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is {price1:.1f}")
print(f"Price 1 is {price2:.2f}")
print(f"Price 1 is {price3:10.3f}")
 
print(f"Price 1 is {price1:<010.1f}")
print(f"Price 1 is {price2:>010.2f}")
print(f"Price 1 is {price3:^010.3f}") #on amount of spaces

print(f"Price 1 is {price1:+}") # to show the sign

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price 1 is {price1:,}")#thousands are separated with comma
print(f"Price 1 is {price2:,.2f}")
print(f"Price 1 is {price3:+,.3f}")