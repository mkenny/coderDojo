# Space Rescue - Step 4: Rescue the astronauts
#
# New in this step:
# - 5 astronauts instead of 1
# - touching an astronaut rescues it: the score goes up and the astronaut goes back to the top
# - a hidden writer turtle shows the score, using show_score()
# - global score, because game_loop() changes the score

import turtle
import random

screen = turtle.Screen()
screen.title("Space Rescue - Step 4")
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

# a hidden turtle that writes the score in the top left corner
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.goto(-330, 310)

score = 0

def make_astronaut():
    astronaut = turtle.Turtle()
    astronaut.shape("circle")
    astronaut.color("gold")
    astronaut.penup()
    astronaut.goto(random.randint(-300, 300), random.randint(0, 350))
    return astronaut

# 5 astronauts, so there's always something to catch
astronauts = []
for i in range(5):
    astronauts.append(make_astronaut())

def show_score():
    # rub out the old score before writing the new one
    writer.clear()
    writer.write("Score: " + str(score), font=("Arial", 18, "bold"))

# the keys don't move the player, they just say which way to go
def go_left():
    player.direction = -1

def go_right():
    player.direction = 1

def stop():
    player.direction = 0

def game_loop():
    # score is a number we change, so we need global to change the one at the top
    global score

    # stop at the edge of the screen
    if player.direction == -1 and player.xcor() > -300:
        player.setx(player.xcor() - 10)
    if player.direction == 1 and player.xcor() < 300:
        player.setx(player.xcor() + 10)

    for astronaut in astronauts:
        astronaut.sety(astronaut.ycor() - 5)

        # caught it! add a point and send the astronaut back to the top
        if astronaut.distance(player) < 20:
            score = score + 1
            show_score()
            astronaut.goto(random.randint(-300, 300), 350)

        # when it falls off the bottom, start again at the top
        elif astronaut.ycor() < -350:
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

show_score()
game_loop()

turtle.done()
