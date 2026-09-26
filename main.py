import random

balance = 100

print("\n" + "-" * 30)
print("!!!! Welcome to the Snake Eyes game !!!!")
print("-" * 30)

while balance > 0:
    print(f"\nCurrent balance: {balance} points")
    choice = input('How many points do you wish to play? (type "quit" to exit) ').strip().lower()

    if choice == "quit":
        print("Thank you for playing!")
        break

    if not choice.isdigit():
        print("Please enter a whole number, such as 5.")
        continue

    points = int(choice)
    if points < 1 or points > balance:
        print(f"Please choose between 1 and {balance} points.")
        continue

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"You rolled: {dice1}, {dice2}")

    if dice1 == 1 and dice2 == 1:
        print("Snake eyes! You earned bonus points!")
        balance = balance + points * 35
    else:
        print(f"You used {points} points.")
        balance = balance - points

if balance == 0:
    print("\nYour balance has run out — game over!")
