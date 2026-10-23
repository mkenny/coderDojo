# Space Rescue - Step 2: A falling astronaut and the game loop
#
# New in this step:
# - an astronaut (a gold circle) made by make_astronaut() and kept in a list
# - game_loop() moves the astronaut down a little, then uses ontimer to run again in 20 milliseconds
# - when the astronaut falls off the bottom, it starts again at the top
# - screen.tracer(0) and screen.update() draw everything at once
# - try holding an arrow key: the astronaut glides, but the player jumps!
# - demos to try: 19 more astronauts, and a while loop instead of ontimer

import turtle
import random

screen = turtle.Screen()
screen.title("Space Rescue - Step 2")
screen.setup(700, 700)
# without screen.tracer(0), turtle redraws the screen after every astronaut moves;
# with it, turtle moves all the astronauts first and redraws the screen just once
screen.tracer(0)

player = turtle.Turtle()
player.shape("square")
player.penup()
player.goto(0, -300)

def make_astronaut():
    astronaut = turtle.Turtle()
    astronaut.shape("circle")
    astronaut.color("gold")
    astronaut.penup()
    astronaut.goto(random.randint(-300, 300), random.randint(0, 350))
    return astronaut

astronauts = [make_astronaut()]

# DEMO: uncomment these two lines to add 19 more astronauts
# for i in range(19):
#     astronauts.append(make_astronaut())

# the astronauts move every time the game loop runs, but the player only moves
# when the keyboard repeats the key press, which is much less often,
# so it jumps instead of gliding
def move_left():
    # stop at the edge of the screen
    if player.xcor() > -300:
        player.setx(player.xcor() - 20)

def move_right():
    if player.xcor() < 300:
        player.setx(player.xcor() + 20)

# the astronauts move a little bit every 20 milliseconds, so they glide
def game_loop():
    for astronaut in astronauts:
        astronaut.sety(astronaut.ycor() - 5)

        # when it falls off the bottom, start again at the top
        if astronaut.ycor() < -350:
            astronaut.goto(random.randint(-300, 300), 350)

    screen.update()
    # run game_loop again in 20 milliseconds. We use this instead of a while
    # loop because in between, turtle is free to listen to the keyboard, and
    # the game runs at the same speed on every computer
    screen.ontimer(game_loop, 20)

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

game_loop()

# DEMO: the same falling astronauts using a while loop instead of ontimer.
# Comment out game_loop() above and uncomment these lines to try it.
# Watch how fast the astronauts fall, and what happens when you close the window.
# while True:
#     for astronaut in astronauts:
#         astronaut.sety(astronaut.ycor() - 5)
#         if astronaut.ycor() < -350:
#             astronaut.goto(random.randint(-300, 300), 350)
#     screen.update()

turtle.done()
