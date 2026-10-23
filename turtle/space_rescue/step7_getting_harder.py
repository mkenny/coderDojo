# Space Rescue - Step 7: Getting harder
#
# New in this step:
# - fall_speed decides how fast astronauts and asteroids fall
# - every 10 rescues, fall_speed goes up by 1 (using %, the remainder)
# - 10 asteroids instead of 3

import turtle
import random

screen = turtle.Screen()
screen.title("Space Rescue - Step 7")
screen.setup(700, 700)
screen.bgpic("assets/space.gif")
# without screen.tracer(0), turtle redraws the screen after every astronaut moves;
# with it, turtle moves all the astronauts first and redraws the screen just once
screen.tracer(0)

# tell turtle about our pictures so we can use them as shapes
screen.register_shape("assets/player.gif")
screen.register_shape("assets/player_left.gif")
screen.register_shape("assets/player_right.gif")
screen.register_shape("assets/astronaut.gif")
screen.register_shape("assets/asteroid.gif")

player = turtle.Turtle()
player.shape("assets/player.gif")
player.penup()
player.goto(0, -300)
# the player keeps its own direction: -1 for left, 1 for right, 0 for standing still
player.direction = 0

# a hidden turtle that writes the score in the top left corner
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("white")
writer.goto(-330, 310)

score = 0
lives = 3
# how far astronauts and asteroids fall each time the game loop runs
fall_speed = 10

def make_astronaut():
    astronaut = turtle.Turtle()
    astronaut.shape("assets/astronaut.gif")
    astronaut.penup()
    astronaut.goto(random.randint(-300, 300), random.randint(0, 350))
    return astronaut

# just like an astronaut, but with an asteroid picture
def make_asteroid():
    asteroid = turtle.Turtle()
    asteroid.shape("assets/asteroid.gif")
    asteroid.penup()
    asteroid.goto(random.randint(-300, 300), random.randint(0, 350))
    return asteroid

# 5 astronauts, so there's always something to catch
astronauts = []
for i in range(5):
    astronauts.append(make_astronaut())

# 10 asteroids to dodge
asteroids = []
for i in range(10):
    asteroids.append(make_asteroid())

def show_score():
    # rub out the old score before writing the new one
    writer.clear()
    writer.write("Score: " + str(score) + "   Lives: " + str(lives), font=("Arial", 18, "bold"))

# the keys don't move the player, they just say which way to go,
# and swap the picture so the rocket leans the way it's moving
def go_left():
    player.direction = -1
    player.shape("assets/player_left.gif")

def go_right():
    player.direction = 1
    player.shape("assets/player_right.gif")

def stop():
    player.direction = 0
    player.shape("assets/player.gif")

def game_loop():
    # score, lives and fall_speed are numbers we change, so we need global to change the ones at the top
    global score, lives, fall_speed

    # stop at the edge of the screen
    if player.direction == -1 and player.xcor() > -300:
        player.setx(player.xcor() - 10)
    if player.direction == 1 and player.xcor() < 300:
        player.setx(player.xcor() + 10)

    for astronaut in astronauts:
        astronaut.sety(astronaut.ycor() - fall_speed)

        # caught it! add a point and send the astronaut back to the top
        if astronaut.distance(player) < 25:
            score = score + 1
            # every 10 points, everything falls a bit faster
            # (% gives the remainder: 10 % 10 is 0, 13 % 10 is 3, 20 % 10 is 0)
            if score % 10 == 0:
                fall_speed = fall_speed + 1
            show_score()
            astronaut.goto(random.randint(-300, 300), 350)

        # when it falls off the bottom, start again at the top
        elif astronaut.ycor() < -350:
            astronaut.goto(random.randint(-300, 300), 350)

    for asteroid in asteroids:
        asteroid.sety(asteroid.ycor() - fall_speed)

        # hit! lose a life and send the asteroid back to the top
        # (asteroids are bigger, so they hit from further away)
        if asteroid.distance(player) < 40:
            lives = lives - 1
            show_score()
            asteroid.goto(random.randint(-300, 300), 350)

        elif asteroid.ycor() < -350:
            asteroid.goto(random.randint(-300, 300), 350)

    screen.update()

    # no lives left: write GAME OVER and don't run the game loop again
    if lives == 0:
        writer.goto(0, 0)
        writer.write("GAME OVER", align="center", font=("Arial", 40, "bold"))
    else:
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
