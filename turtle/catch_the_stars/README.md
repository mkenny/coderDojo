# Catch the Stars

**In this exercise you will:**

- Move a turtle with the arrow keys.
- Use a game loop with `ontimer` so the game keeps running while you press keys.
- Make stars and rocks fall from the sky, and catch them with your turtle.
- Keep score, lose lives, and make the game get harder as you go.

This builds on the [turtle race](../turtle_race/): you'll use functions that make turtles, lists of turtles, `random`, and `distance()` again.

## The game

You control a turtle at the bottom of the screen. Gold stars and grey rocks fall from the top. Catch a star to score a point; catch a rock and you lose a life. Lose all three lives and it's game over. The more stars you catch, the faster everything falls.

## Run the game

    python3 catch_the_stars.py

Use the **Left** and **Right** arrow keys to move.

## Build it yourself

Start with `catch_the_stars.py`, which opens the game window. Run your code after each step to check it still works.

### Step 1: Make the player move

- Make a turtle called `player`, give it `shape("turtle")`, lift its pen, turn it to face up with `setheading(90)`, and move it to `(0, -250)`.
- Write two functions, `move_left()` and `move_right()`, that change the player's x position by 20 steps using `setx()` and `xcor()`.
- Tell the screen to listen for keys with `screen.listen()`, then connect your functions to the keys: `screen.onkey(move_left, "Left")` and `screen.onkey(move_right, "Right")`.
- Stop the player going off the edge: only move if the new x would be between `-380` and `380`.

### Step 2: Make one star fall

- Write a function called `make_star()` that makes a small gold `"circle"` turtle, lifts its pen and puts it at a random x across the top of the screen (y = `300`).
- Write a function called `game_loop()` that moves the star down 5 steps with `sety()`.
- At the end of `game_loop()`, call `screen.ontimer(game_loop, 20)` so it runs again in 20 milliseconds. Call `game_loop()` once, just before `turtle.done()`, to start it off.
- When the star gets below `-300`, move it back to a random spot at the top.

### Step 3: Lots of stars, and catching them

- Add `screen.tracer(0)` near the top, and `screen.update()` at the end of `game_loop()`. This draws everything at once so the game doesn't flicker.
- Make an empty list called `stars`. In `game_loop()`, give a 1 in 20 chance of adding a new star with `make_star()`.
- Loop over a copy of the list (`stars[:]`) and move every star down.
- If a star is less than `20` away from the player, add 1 to `score`, hide the star and remove it from the list. Do the same for stars that fall off the bottom.

### Step 4: Show the score

- Make a hidden turtle called `writer` and move it to the top left of the screen.
- Write a function called `show_score()` that calls `writer.clear()` and then `writer.write()` with the score.
- Call `show_score()` whenever the score changes.

### Step 5: Rocks, lives and game over

- Make rocks the same way as stars, but grey and in their own list called `rocks`.
- Start with `lives = 3`. Catching a rock takes away a life. Show the lives next to the score.
- When `lives` reaches `0`, write `GAME OVER` in the middle of the screen and don't call `ontimer` again, so the game stops.

### Step 6: Make it harder

- Make a variable called `fall_speed`, starting at `5`, and use it instead of `5` when things fall.
- Every time the score goes up by 10, add 1 to `fall_speed`.

## Ideas for extra challenges

- Keep a high score in a file so it's remembered after you close the game.
- Add a rare power-up that gives an extra life or makes the player bigger for a while.
- Let the player press **Space** to start a new game after game over.
- Make a two-player version with a second turtle on the **A** and **D** keys.
