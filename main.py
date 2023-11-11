print()

cents = int(input("Enter the number of cents [1-99]: "))

print("\nCoins used:")

while cents > 0:
  if cents >= 25:
    cents = cents - 25
    print("quarter")
  elif cents >= 10:
    cents = cents - 10
    print("dime")
  elif cents >= 5:
    cents = cents - 5
    print("nickel")
  else:
    cents = cents - 1
    print("penny")
