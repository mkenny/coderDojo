from auto_roll import auto_roll
from snake_eyes import play_game


def main():
    print("\n" + "-" * 30)
    print("!!!! Welcome to the Snake Eyes game !!!!")
    print("-" * 30)
    print("1. Play the game")
    print("2. Auto roll the dice to see win percentages")

    while True:
        choice = input("Choose 1 or 2: ").strip()
        if choice == "1":
            play_game()
            break
        if choice == "2":
            auto_roll()
            break
        print("Please enter 1 or 2.")


if __name__ == "__main__":
    main()
