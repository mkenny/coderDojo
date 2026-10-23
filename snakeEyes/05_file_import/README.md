# Snake Eyes

A dice game. Bet some points and roll two dice. If both dice land on 1 ("snake eyes"), you win 35 times your bet. Any other roll loses your bet.

There's also an auto roll mode that rolls the dice many times and shows how often snake eyes comes up.

## Run the game

    python3 main.py

## Run the tests

From this folder (not inside `tests/`):

    python3 -m unittest -v

## Files

| File | What it does |
|---|---|
| `main.py` | Shows the menu and starts the game or auto roll |
| `snake_eyes.py` | The Snake Eyes game |
| `auto_roll.py` | Rolls the dice many times and shows the win percentage |
| `tests/` | Tests that check the code works |

## Build it yourself

Follow these steps to write the game from scratch. Test each step by running your code before moving on.

### Step 1: Roll two dice (`snake_eyes.py`)

- Import the `random` module.
- Use `random.randint(1, 6)` to roll two dice and store them in `dice1` and `dice2`.
- Print what was rolled, for example `You rolled: 3, 5`.

### Step 2: Check for snake eyes

- Use an `if` statement to check whether both dice are 1.
- Print `Snake eyes!` if they are, and something else if they aren't.

### Step 3: Write `calculate_balance()`

- Write a function `calculate_balance(balance, points, dice1, dice2)` that returns the new balance:
  - Snake eyes: add `points * 35` to the balance.
  - Anything else: subtract `points` from the balance.
- Store `35` in a variable at the top of the file, such as `SNAKE_EYES_MULTIPLIER`, so it's easy to change.

### Step 4: Ask for a starting balance

- Use `input()` to ask the player how many points they want to start with.
- Keep asking until they enter a whole number of at least 1. Hint: `.isdigit()` checks whether text is a whole number.

### Step 5: Make the game loop

- Use a `while` loop that keeps going while the balance is above 0.
- Each time round the loop:
  1. Show the current balance.
  2. Ask how many points to bet. The bet must be between 1 and the current balance.
  3. Roll the dice and print the result.
  4. Use `calculate_balance()` to update the balance.
- When the balance reaches 0, print `Game over!`.

### Step 6: Let the player quit

- If the player types `quit` instead of a bet, print a goodbye message and `break` out of the loop.
- Only print `Game over!` if the balance really is 0, not when the player quit.

### Step 7: Put the game in a function

- Move all the game code (steps 4 to 6) into a function called `play_game()`.
- At the bottom of the file, add:

      if __name__ == "__main__":
          play_game()

  This runs the game when you start `snake_eyes.py` directly, but not when another file imports it.

### Step 8: Auto roll (`auto_roll.py`)

- Create a new file with a function `auto_roll()`.
- Ask how many times to roll the dice.
- Use a `for` loop to roll two dice that many times, counting how many rolls were snake eyes.
- Work out the percentage: `wins / rolls * 100`.
- Print the result, and compare it with the expected chance: 1 in 36, about 2.78%.
- Try 10 rolls, then 1,000, then 100,000. What happens to the percentage?

### Step 9: The menu (`main.py`)

- Import `play_game` from `snake_eyes` and `auto_roll` from `auto_roll`.
- Print a welcome message and a menu:

      1. Play the game
      2. Auto roll the dice to see win percentages

- Keep asking until the player enters 1 or 2, then call the right function.

### Step 10: Write a test (`tests/test_snake_eyes.py`)

- Create a `tests` folder with an empty file called `__init__.py`.
- Write a test that checks `calculate_balance()` gives the right answer. For example, a balance of 100 with a bet of 10:
  - Rolling 1 and 1 should give 450.
  - Rolling 3 and 4 should give 90.
- Run the tests with `python3 -m unittest -v`.

## Ideas for extra challenges

- Draw the dice as pictures using text characters.
- Pay out 5 times the bet for any other double (2 and 2, 3 and 3, and so on).
- Add a second player who takes turns with you.
- Ask "Play again?" when the game ends.
