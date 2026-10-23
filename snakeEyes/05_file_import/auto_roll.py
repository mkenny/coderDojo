import random


def auto_roll():
    while True:
        choice = input("How many times should the dice be rolled? ").strip()
        if choice.isdigit() and int(choice) >= 1:
            rolls = int(choice)
            break
        print("Please enter a whole number of at least 1.")

    wins = 0
    for roll in range(rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 == 1 and dice2 == 1:
            wins = wins + 1

    percentage = wins / rolls * 100
    print(f"\nRolled the dice {rolls} times.")
    print(f"Snake eyes came up {wins} times: {percentage:.2f}%")
    print("The expected chance is 1 in 36: about 2.78%")


if __name__ == "__main__":
    auto_roll()
