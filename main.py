import random

STARTING_BALANCE = 100
SNAKE_EYES_MULTIPLIER = 35


def is_snake_eyes(dice1, dice2):
    return dice1 == 1 and dice2 == 1


def calculate_new_balance(balance, points_to_play, dice1, dice2):
    if is_snake_eyes(dice1, dice2):
        return balance + points_to_play * SNAKE_EYES_MULTIPLIER

    return balance - points_to_play


def ask_points_to_play(balance):
    """Prompt until the player enters a valid bet. Returns None if they quit."""
    while True:
        user_choice = input(
            'How many points do you wish to play? (type "quit" to exit) '
        ).strip().lower()

        if user_choice == "quit":
            return None

        try:
            points_to_play = int(user_choice)
        except ValueError:
            print("Please enter a whole number, such as 5.")
            continue

        if points_to_play <= 0:
            print("Please choose at least 1 point.")
        elif points_to_play > balance:
            print("You cannot play more points than you have.")
        else:
            return points_to_play


def main():
    balance = STARTING_BALANCE

    print("\n" + "-" * 30)
    print("!!!! Welcome to the Snake Eyes game !!!!")
    print("-" * 30)

    while balance > 0:
        print(f"\nCurrent balance: {balance} points")

        points_to_play = ask_points_to_play(balance)
        if points_to_play is None:
            print("Thank you for playing!")
            return

        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"You rolled: {dice1}, {dice2}")

        if is_snake_eyes(dice1, dice2):
            print("Snake eyes! You earned bonus points!")
        else:
            print(f"You used {points_to_play} points.")

        balance = calculate_new_balance(balance, points_to_play, dice1, dice2)

    print("\nYour balance has run out — game over!")


if __name__ == "__main__":
    main()
