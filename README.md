# Snake Eyes

A dice game. You start with 100 points. Choose how many points to play and roll two dice. If both dice land on 1 ("snake eyes"), you win 35 times the points you played. Any other roll and you lose the points you played.

## Run the game

    python3 main.py

## Build it yourself

Follow these steps to write the game from scratch in `main.py`. Run your code after each step to check it works before moving on.

### Step 1: Welcome the player

- Print a welcome message, for example `Welcome to the Snake Eyes game`.
- Hint: `"-" * 30` makes a line of 30 dashes to use as a border.

### Step 2: Roll two dice

- Import the `random` module at the top of the file.
- Use `random.randint(1, 6)` to roll two dice and store them in `dice1` and `dice2`.
- Print what was rolled, for example `You rolled: 3, 5`.

### Step 3: Check for snake eyes

- Use an `if` statement to check whether both dice are 1.
- Print `Snake eyes!` if they are, and something else if they aren't.

### Step 4: Keep score

- Create a variable `balance` and set it to 100.
- Create a variable `points` for the number of points to play. Set it to 10 for now.
- If the roll is snake eyes, add `points * 35` to the balance. Otherwise, subtract `points`.
- Print the new balance.

### Step 5: Ask the player how many points to play

- Replace the fixed 10 with `input()`, asking how many points they want to play.
- `input()` gives you text, so turn it into a number with `int()`.

### Step 6: Keep playing

- Put the code for choosing points and rolling the dice inside a `while` loop that keeps going while the balance is above 0.
- Show the current balance at the start of each turn.
- When the loop ends, print `Game over!`.

### Step 7: Check the number is valid

- If the player types something that isn't a number, print a message and ask again. Hint: `.isdigit()` checks whether text is a whole number, and `continue` jumps back to the start of the loop.
- If the number is less than 1 or more than their balance, print a message and ask again.

### Step 8: Let the player quit

- If the player types `quit` instead of a number, print a goodbye message and use `break` to leave the loop.
- Only print `Game over!` if the balance really is 0, not when the player quit.

## Ideas for extra challenges

- Let the player choose their starting balance.
- Draw the dice as pictures using text characters.
- Give 5 times the points played for any other double (2 and 2, 3 and 3, and so on).
- Roll the dice 1,000 times automatically and count how often snake eyes comes up. Is it close to 1 in 36?
