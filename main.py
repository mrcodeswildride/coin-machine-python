print()

cents = int(input("Enter the number of cents [1-99]: "))

coins = ""

while cents > 0:
  if cents >= 25:
    cents = cents - 25
    coins = coins + "quarter "
  elif cents >= 10:
    cents = cents - 10
    coins = coins + "dime "
  elif cents >= 5:
    cents = cents - 5
    coins = coins + "nickel "
  else:
    cents = cents - 1
    coins = coins + "penny "

print(f"\n{coins}")
