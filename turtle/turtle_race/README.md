# Turtle Race

**In this exercise you will:**

- Draw a race track with a finish line.
- Use a function and a loop to make five racing turtles.
- Ask the player to bet on a winner, then race the turtles until one crosses the line.
- Add power-ups that speed a turtle up or slow it down.

## The game

Five turtles (red, green, blue, pink and yellow) line up on the left of the screen. Before the race you guess which one will win. Each turtle moves forward a random distance every turn, so anyone can win. Along the way, power-ups appear in the lanes: **gold** ones push a turtle 50 steps forward, **black** ones push it 50 steps back. The first turtle to reach the finish line wins, and the screen tells you whether your bet was right.

## Run the game

    python3 turtle_race.py

Type a colour exactly as shown (for example `red`) when asked who will win.

## Build it yourself

Start with a new file called `turtle_race.py`. Run your code after each step to check it still works.

### Step 1: Set up the screen and finish line

- `import turtle` and `import random` at the top.
- Make a screen with `turtle.Screen()`, give it a background colour with `bgcolor()`, and set its size to 800 by 600 with `setup()`.
- Write a function called `draw_finishline()` that makes a hidden turtle, lifts its pen, moves to `(300, -150)`, puts the pen down and draws up to `(300, 150)`.
- Call the function, and put `turtle.done()` at the very end of the file so the window stays open.

### Step 2: Make the racers

- Make a list called `colours` with five colours in it.
- Write a function called `make_racer(colour, y)` that makes a turtle, sets its `shape("turtle")` and `color(colour)`, lifts the pen, moves it to `(-300, y)` and `return`s it.
- Use a `for` loop over `colours` to make one racer per colour and add each one to a list called `racers`. Start `y` at `120` and take away `60` each time round the loop so every turtle gets its own lane.

### Step 3: Ask for a bet

- Before the racers are made, use `screen.textinput()` to ask "Who will win?" and store the answer in a variable called `bet`.

### Step 4: Race!

- Make a variable `winner = False`.
- Use a `while` loop that keeps going until there is a winner. Inside it, loop over `racers` and move each one `forward()` by `random.randint(1, 10)`.
- After each move, check if the racer's `xcor()` is `300` or more. If it is, save its colour (`racer.pencolor()`) as the winner, set `winner = True` and `break`.

### Step 5: Show the result

- Make a hidden turtle called `writer`.
- If `bet` matches the winning colour, make a "you win" message; otherwise make a "you lose" message that says who won.
- Use `writer.write()` to show the message in the middle of the screen with a big font.

### Step 6: Add power-ups

- Write a function called `make_powerup(y)` that makes a small circle turtle at a random `x` between `-200` and `250` in lane `y`. Use `random.choice(["gold", "black"])` for its colour. Hint: make it with `turtle.Turtle(visible=False)` and call `showturtle()` once it's in place, so it doesn't flash up in the middle of the screen.
- Make an empty list called `powerups`.
- At the start of each turn in the race loop, give a 1 in 15 chance of a new power-up appearing in a random racer's lane, using `random.randint(1, 15) == 1`.
- After a racer moves, check every power-up: if `racer.distance(powerup)` is less than `10`, move the racer `forward(50)` for gold or `backward(50)` for black, then hide the power-up and remove it from the list.
- Give each power-up a 1 in 40 chance of disappearing each turn, even if no one reaches it.
- Hint: when you remove items from a list while looping over it, loop over a copy instead: `for powerup in powerups[:]:`

## Ideas for extra challenges

- What happens if you type `Red` or press Cancel when asked for a bet? Make the game keep asking until it gets one of the colours.
- Add a sixth turtle. What else do you need to change so it fits on the track?
- Add a new kind of power-up, such as one that sends a turtle back to the start.
- Keep score over several races and show how many bets the player got right.
