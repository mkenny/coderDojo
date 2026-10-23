# Space Rescue

**In this exercise you will:**

- Move a player with the arrow keys.
- Use a game loop with `ontimer` so things keep moving while you press keys.
- Make astronauts and asteroids fall from the sky, and rescue the astronauts.
- Keep score, lose lives, use your own pictures, and make the game get harder as you go.
- Add a fuel gauge, sounds and an explosion.

This builds on the [turtle race](../turtle_race/): you'll use functions that make turtles, lists of turtles, `random`, and `distance()` again.

## The game

You fly a starship along the bottom of the screen. Astronauts float down from the top, along with dangerous asteroids. Fly into an astronaut to rescue them and score a point; get hit by an asteroid and you lose a life. The ship burns fuel as it flies, so collect fuel cells to keep the tank topped up. Lose all three lives or run out of fuel and it's game over. Every 10 astronauts you rescue, everything falls a bit faster.

## Run the game

Go into this folder first, so the game can find its pictures and sounds (the sounds only work on a Mac):

    cd space_rescue
    python3 space_rescue.py

Hold the **Left** and **Right** arrow keys to move. If the keys don't work, click on the game window first.

## What's in this folder

- `space_rescue.py` – the finished game (the same as Step 9)
- `step1_move_player.py` to `step9_sounds.py` – the game built up one step at a time. Each file is the one before it plus one new idea, so you can run any of them to see how far you've got. The comment at the top of each file lists what's new in that step.
- `assets/` – all the pictures and sounds. In the code, their names start with `assets/`, for example `"assets/player.gif"`.
  - Pictures (they must be `.gif` files for turtle to use them):
    - `space.gif` – the background
    - `player.gif`, `player_left.gif`, `player_right.gif` – the ship flying straight and leaning each way
    - `astronaut.gif`, `asteroid.gif`, `fuel.gif` – the falling things
    - `damage1.gif`, `damage2.gif` – damage shown on the ship after each asteroid hit
    - `explosion.gif` – shown when the ship explodes at game over
  - Sounds (used in Step 9): `rocket.wav` (the engine), `rescue.wav`, `fuel.wav`, `hit.wav` and `gameover.wav`

## Build it yourself

Start with a new file (for example `my_space_rescue.py`) and build the game a step at a time. Run your code after each step to check it still works. If you get stuck, open the step file with the same number to see one way of doing it.

### Step 1: Move the player (`step1_move_player.py`)

- `import turtle` at the top. Make a screen, give it a title, and make it 700 by 700 with `screen.setup(700, 700)`.
- Make a turtle called `player`, give it `shape("square")`, lift its pen and move it to `(0, -300)`.
- Write two functions, `move_left()` and `move_right()`, that move the player 20 steps with `setx()` and `xcor()`.
- Stop the player going off the edge: in `move_left()`, only move if `player.xcor() > -300`. In `move_right()`, only move if `player.xcor() < 300`. The window goes from `-350` to `350`, so this leaves space for the player.
- Turn on the keyboard with `screen.listen()`, then connect your functions to the keys with `screen.onkeypress(move_left, "Left")` and `screen.onkeypress(move_right, "Right")`.
- Put `turtle.done()` at the very end so the window stays open.

### Step 2: A falling astronaut and the game loop (`step2_falling_astronaut.py`)

Until Step 6 we keep things simple: a plain background, a square for the player, and gold circles for the astronauts.

- `import random` at the top.
- Write a function called `make_astronaut()` that makes a gold `"circle"` turtle, lifts its pen, puts it at a random spot near the top of the screen and returns it. Make a list with one astronaut in it: `astronauts = [make_astronaut()]`.
- Write a function called `game_loop()` that moves every astronaut in `astronauts` down 5 steps with `sety()`. When one falls below `-350`, send it back to a random spot at the top (y = `350`).
- At the end of `game_loop()`, call `screen.ontimer(game_loop, 20)` so it runs again in 20 milliseconds. Call `game_loop()` once, just before `turtle.done()`, to start it off.
- Add `screen.tracer(0)` near the top, and `screen.update()` in `game_loop()` just before `ontimer`. Without `tracer(0)`, turtle redraws the screen after every astronaut moves; with it, turtle moves them all first and redraws the screen just once.

**Try this:** hold an arrow key. The astronaut glides, but the player jumps! The astronaut moves every time the game loop runs, but the player only moves when the keyboard repeats the key press, which is much less often.

**Demos in this file:**

- Uncomment the lines that add 19 more astronauts. Then comment out `screen.tracer(0)` and see how slow it gets with lots of things moving.
- Comment out `game_loop()` and uncomment the `while True:` loop at the bottom to see why we use `ontimer` instead: things fall at a different speed on every computer, and closing the window gives an error.

### Step 3: Smooth movement (`step3_smooth_player.py`)

Let the game loop move the player too, a little bit every time it runs, just like the astronauts.

- Give the player its own direction with `player.direction = 0`. It will be `-1` for left, `1` for right and `0` for standing still.
- Swap `move_left()` and `move_right()` for three small functions: `go_left()` sets `player.direction = -1`, `go_right()` sets it to `1`, and `stop()` sets it to `0`.
- Connect them to the keys going down (`onkeypress`) and coming back up (`onkeyrelease`):

      screen.onkeypress(go_left, "Left")
      screen.onkeypress(go_right, "Right")
      screen.onkeyrelease(stop, "Left")
      screen.onkeyrelease(stop, "Right")

- At the start of `game_loop()`, move the player 10 steps left if `player.direction == -1` and it's not at the left edge, and 10 steps right if `player.direction == 1` and it's not at the right edge.

### Step 4: Rescue the astronauts (`step4_rescue_astronauts.py`)

- Make 5 astronauts instead of 1: start with an empty list, `astronauts = []`, and use a `for` loop to add 5 with `astronauts.append(make_astronaut())`.
- Make `score = 0` at the top.
- Make a hidden turtle called `writer` and move it to the top left of the screen, at `(-330, 310)`.
- Write a function called `show_score()` that calls `writer.clear()` to rub out the old score, then `writer.write()` with the new one. Call it once at the start.
- In the astronaut loop, if an astronaut is less than `20` away from the player, add 1 to `score`, call `show_score()`, and send the astronaut back to the top.
- Add `global score` at the top of `game_loop()`. `score` is a number we change, so Python needs to know we mean the one at the top of the file.

### Step 5: Asteroids, lives and game over (`step5_asteroids_and_lives.py`)

- Write a function called `make_asteroid()`. It's just like `make_astronaut()`, but grey and bigger (`shapesize(1.5)`). Make a list of 3 asteroids.
- Make `lives = 3` at the top, and show the lives next to the score.
- In `game_loop()`, move the asteroids down just like the astronauts. If an asteroid is less than `25` away from the player (asteroids are bigger, so they hit from further away), take away a life and send it back to the top.
- Add `lives` to the `global` line.
- At the end of `game_loop()`, if `lives` is `0`, write `GAME OVER` in the middle of the screen. Otherwise call `ontimer` as usual. If we don't call `ontimer`, the game loop doesn't run again, so the game stops.

### Step 6: Pictures (`step6_images.py`)

- Add `screen.bgpic("assets/space.gif")` for the background. The pictures are in the `assets` folder, so their names start with `assets/`.
- Register all the pictures with `screen.register_shape()`: `assets/player.gif`, `assets/player_left.gif`, `assets/player_right.gif`, `assets/astronaut.gif` and `assets/asteroid.gif`.
- Use the pictures instead of shapes: `player.shape("assets/player.gif")`, `astronaut.shape("assets/astronaut.gif")` and `asteroid.shape("assets/asteroid.gif")`. You can delete the `color()` and `shapesize()` lines for the astronauts and asteroids.
- Make the ship lean the way it's moving: in `go_left()` add `player.shape("assets/player_left.gif")`, in `go_right()` add `player.shape("assets/player_right.gif")`, and in `stop()` add `player.shape("assets/player.gif")`.
- Make the writing white with `writer.color("white")` so you can see it on the dark background.
- The pictures are a different size to the shapes, so change the rescue distance to `25` and the asteroid distance to `40`.

### Step 7: Getting harder (`step7_getting_harder.py`)

- Make a variable called `fall_speed` and use it instead of `5` when astronauts and asteroids fall. The step file starts it at `10` and has 10 asteroids, for a much harder game. Try `5` and 3 asteroids if that's too hard.
- When you rescue an astronaut, check `if score % 10 == 0:` and add 1 to `fall_speed`. `%` gives the remainder after dividing, so `score % 10` is `0` at 10, 20, 30 and so on.
- Add `fall_speed` to the `global` line.

### Step 8: A fuel gauge (`step8_fuel.py`)

The ship now uses up fuel as it flies. Collect fuel cells to top it up. If the tank runs dry, it's game over, even if you still have lives left.

- Register `assets/fuel.gif`, write a `make_fuel_cell()` function (just like `make_astronaut()`, with the fuel picture) and make a list with 1 fuel cell in it.
- Make `fuel = 100` at the top: 100 means full, 0 means empty. Add `fuel` to the `global` line.
- In `game_loop()`, take a little fuel away every time: `fuel = fuel - 0.2`.
- Move the fuel cells down like the astronauts. If one is less than `25` away from the player, add `20` to `fuel`, but don't let it go above `100`.
- If `fuel` goes below `0`, set it back to `0`.
- Make a hidden turtle called `gauge`, and write a `draw_gauge()` function that clears it, writes "Fuel", and draws a filled box with `begin_fill()` and `end_fill()` that is `fuel * 2` steps wide. Make it green when there's lots of fuel, orange when it's getting low and red when it's nearly empty. Draw a white outline 200 steps wide to show a full tank. Call `draw_gauge()` every time the game loop runs.
- Change the game over check to `if lives == 0 or fuel == 0:`.

### Step 9: Sounds, floating astronauts and an explosion (`step9_sounds.py`)

- `import subprocess` at the top. It lets Python run other programs, like the Mac's `afplay` sound player.
- Write `play_sound(sound_file)`, which runs `subprocess.Popen(["afplay", sound_file])`. This plays a sound without pausing the game. Call it when you rescue an astronaut (`assets/rescue.wav`), collect fuel (`assets/fuel.wav`), get hit (`assets/hit.wav`) and at game over (`assets/gameover.wav`).
- Start the engine sound at the top with `engine = subprocess.Popen(["afplay", "assets/rocket.wav"])`. Write `keep_engine_running()`, which starts it again when it has finished (`engine.poll()` is `None` while a sound is still playing), and call it every time the game loop runs. At game over, stop it with `engine.terminate()`.
- Swap `make_astronaut()`, `make_fuel_cell()` and `make_asteroid()` for one function, `make_thing(picture)`. They were all the same apart from the picture, so now you just say which picture you want: `make_thing("assets/astronaut.gif")`.
- Make the astronauts float: give each one `astronaut.drift = random.choice([-1, 1])`, then in the game loop move it sideways by `astronaut.drift` each time. Turn it round (`astronaut.drift = -astronaut.drift`) at the edges, and now and then for no reason.
- Shake the ship when an asteroid hits it: move it 5 steps left, then use `screen.ontimer(bump_back, 100)` to run a `bump_back()` function 100 milliseconds later that moves it 5 steps right again.
- Show damage after each hit: register `assets/damage1.gif` and `assets/damage2.gif`, and make a hidden turtle called `damage`. At the end of `game_loop()`, move it onto the ship, then use `lives` to choose the picture: `damage1.gif` (and `showturtle()`) when `lives == 2`, and `damage2.gif` when `lives == 1`. It's made after the ship, so it's drawn on top, like a sticker.
- Make the ship explode at game over: register `assets/explosion.gif`, make a hidden turtle called `explosion` with that picture, and when the game ends, move it to the ship with `explosion.goto(player.xcor(), player.ycor())`, show it with `showturtle()`, and call `screen.update()` so it appears straight away. The explosion turtle is made after the ship, so turtle draws it on top.

`afplay` only works on a Mac. On Windows, the sounds need different code.

That's the whole game: Step 9 is the same as `space_rescue.py`.

## Use your own pictures and sounds

- Pictures must be `.gif` files. If you have a `.png`, convert it first (for example at [ezgif.com](https://ezgif.com/png-to-gif)).
- Use a transparent background, and keep them small: about 20 to 60 pixels across. Turtle can't resize or turn pictures, so they appear exactly as big as the file.
- Put the picture in the `assets` folder, then use `screen.register_shape("assets/name.gif")` and `shape("assets/name.gif")`.
- If your picture is a different size, change the rescue distance to match.
- Sounds can be `.wav` files. Put them in the `assets` folder and play them with `play_sound("assets/name.wav")`.

## Ideas for extra challenges

- More asteroids as your score goes up, or asteroids that fall faster than astronauts.
- Lose a point when an astronaut floats away off the bottom.
- Keep a high score in a file so it's remembered after you close the game.
- Add a rare power-up that gives an extra life.
- Let the player press **Space** to start a new game after game over.
- Make a two-player version with a second ship on the **A** and **D** keys.
