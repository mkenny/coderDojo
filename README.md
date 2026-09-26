# Snake Eyes: Functions

**In this exercise you will:**

- Add a function to work out the player's new balance after each roll.
- Let the player choose how many points they start with, instead of always starting with 100.

This builds on the game from the `snakeEyesBasic` branch.

## The game

A dice game. Choose how many points to start with, then choose how many points to play and roll two dice. If both dice land on 1 ("snake eyes"), you win 35 times the points you played. Any other roll and you lose the points you played.

## Run the game

    python3 main.py

## Build it yourself

Start with your finished game from the `snakeEyesBasic` branch. Run your code after each step to check it still works.

### Step 1: Write a function to work out the new balance

- At the top of the file, under `import random`, write a function called `calculate_balance(balance, points, dice1, dice2)`.
- It should `return` the new balance:
  - Snake eyes: the balance plus `points * 35`.
  - Anything else: the balance minus `points`.
- Store `35` in a variable above the function, such as `SNAKE_EYES_MULTIPLIER`, so it's easy to change.
- Try it out: `print(calculate_balance(100, 10, 1, 1))` should print `450`, and `print(calculate_balance(100, 10, 3, 4))` should print `90`. Remove these lines once it works.

### Step 2: Use the function in the game

- In your game loop, find the lines that add to or take away from the balance.
- Replace them with one line that calls your function:

      balance = calculate_balance(balance, points, dice1, dice2)

- Keep the `if` that prints `Snake eyes!`, but it no longer needs to change the balance itself.

### Step 3: Let the player choose their starting points

- Replace `balance = 100` with a question using `input()`: how many points do they want to start with?
- Keep asking until they enter a whole number of at least 1. Hint: a `while True` loop with `break` keeps asking until the answer is good.

## Ideas for extra challenges

- Give 5 times the points played for any other double (2 and 2, 3 and 3, and so on). Which part of the code do you need to change?
- Write a test that checks `calculate_balance()` gives the right answers.
