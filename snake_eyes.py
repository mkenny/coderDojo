import random

SNAKE_EYES_MULTIPLIER = 35


def calculate_balance(balance, points, dice1, dice2):
    if dice1 == 1 and dice2 == 1:
        return balance + points * SNAKE_EYES_MULTIPLIER
    return balance - points


def play_game():
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

        if dice1 == 1 and dice2 == 1:
            print("Snake eyes! You earned bonus points!")
        else:
            print(f"You used {points} points.")

        balance = calculate_balance(balance, points, dice1, dice2)

    if balance == 0:
        print("\nYour balance has run out — game over!")


if __name__ == "__main__":
    play_game()
