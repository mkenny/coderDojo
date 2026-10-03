import random

SNAKE_EYES_MULTIPLIER = 35


def calculate_balance(balance, points, dice1, dice2):
    if dice1 == 1 and dice2 == 1:
        return balance + points * SNAKE_EYES_MULTIPLIER
    return balance - points


def draw_dice(number):
    faces = {
        1: ["       ", "   o   ", "       "],
        2: [" o     ", "       ", "     o "],
        3: [" o     ", "   o   ", "     o "],
        4: [" o   o ", "       ", " o   o "],
        5: [" o   o ", "   o   ", " o   o "],
        6: [" o   o ", " o   o ", " o   o "],
    }
    if number not in faces:
        raise ValueError("A dice face must be a number from 1 to 6.")

    lines = ["+-------+"]
    for row in faces[number]:
        lines.append("|" + row + "|")
    lines.append("+-------+")
    return "\n".join(lines)


print("\n" + "-" * 30)
print("!!!! Welcome to the Snake Eyes game !!!!")
print("-" * 30)

while True:
    choice = input("How many points do you want to start with? ").strip()
    if choice.isdigit() and int(choice) >= 1:
        balance = int(choice)
        break
    print("Please enter a whole number of at least 1.")

while balance > 0:
    print(f"\nCurrent balance: {balance} points")
    choice = input('How many points do you wish to play? (type "quit" to exit) ').strip().lower()

    if choice == "quit":
        print("Thank you for playing!")
        break

    if not choice.isdigit() or not 1 <= int(choice) <= balance:
        print(f"Please enter a number between 1 and {balance}.")
        continue

    points = int(choice)
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"You rolled: {dice1}, {dice2}")
    print(draw_dice(dice1))
    print(draw_dice(dice2))

    if dice1 == 1 and dice2 == 1:
        print("Snake eyes! You earned bonus points!")
    else:
        print(f"You used {points} points.")

    balance = calculate_balance(balance, points, dice1, dice2)

if balance == 0:
    print("\nYour balance has run out — game over!")
