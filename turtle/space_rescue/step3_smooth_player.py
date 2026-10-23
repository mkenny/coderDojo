# Space Rescue - Step 3: Smooth movement
#
# New in this step:
# - player.direction remembers which way to go: -1 for left, 1 for right, 0 for standing still
# - the keys just change player.direction, using go_left(), go_right() and stop()
# - onkeyrelease() calls stop() when you let go of a key
# - game_loop() moves the player a little every time it runs, so it glides like the astronaut

import turtle
import random

screen = turtle.Screen()
screen.title("Space Rescue - Step 3")
screen.setup(700, 700)
# without screen.tracer(0), turtle redraws the screen after every astronaut moves;
# with it, turtle moves all the astronauts first and redraws the screen just once
screen.tracer(0)

player = turtle.Turtle()
player.shape("square")
player.penup()
player.goto(0, -300)
# the player keeps its own direction: -1 for left, 1 for right, 0 for standing still
player.direction = 0

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

# the keys don't move the player any more, they just say which way to go
def go_left():
    player.direction = -1

def go_right():
    player.direction = 1

def stop():
    player.direction = 0

def game_loop():
    # the player now moves every time the game loop runs, just like the astronauts,
    # so it glides instead of jumping
    # stop at the edge of the screen
    if player.direction == -1 and player.xcor() > -300:
        player.setx(player.xcor() - 10)
    if player.direction == 1 and player.xcor() < 300:
        player.setx(player.xcor() + 10)

    for astronaut in astronauts:
        astronaut.sety(astronaut.ycor() - 5)

        # when it falls off the bottom, start again at the top
        if astronaut.ycor() < -350:
            astronaut.goto(random.randint(-300, 300), 350)

    screen.update()
    screen.ontimer(game_loop, 20)

screen.listen()
# key goes down: start moving
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")
# key comes back up: stop
screen.onkeyrelease(stop, "Left")
screen.onkeyrelease(stop, "Right")

game_loop()

turtle.done()
