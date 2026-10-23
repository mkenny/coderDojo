# Space Rescue - Step 8: A fuel gauge
#
# New in this step:
# - fuel starts at 100 and goes down a little every time the game loop runs
# - a fuel cell to collect: it tops the tank up by 20, but never past 100
# - draw_gauge() draws a fuel bar that turns orange, then red, as the tank empties
# - GAME OVER if you run out of lives or out of fuel

import turtle
import random

screen = turtle.Screen()
screen.title("Space Rescue - Step 8")
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
screen.register_shape("assets/fuel.gif")
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

# a hidden turtle that draws the fuel gauge in the top right corner
gauge = turtle.Turtle()
gauge.hideturtle()
gauge.penup()

score = 0
lives = 3
# the tank starts full: 100 means full, 0 means empty
fuel = 100
# how far astronauts and asteroids fall each time the game loop runs
fall_speed = 10

def make_astronaut():
    astronaut = turtle.Turtle()
    astronaut.shape("assets/astronaut.gif")
    astronaut.penup()
    astronaut.goto(random.randint(-300, 300), random.randint(0, 350))
    return astronaut

# just like an astronaut, but with a fuel cell picture
def make_fuel_cell():
    cell = turtle.Turtle()
    cell.shape("assets/fuel.gif")
    cell.penup()
    cell.goto(random.randint(-300, 300), random.randint(0, 350))
    return cell

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

# just 1 fuel cell, so it's much harder to find than astronauts
fuel_cells = []
for i in range(1):
    fuel_cells.append(make_fuel_cell())

# 10 asteroids to dodge
asteroids = []
for i in range(10):
    asteroids.append(make_asteroid())

def show_score():
    # rub out the old score before writing the new one
    writer.clear()
    writer.write("Score: " + str(score) + "   Lives: " + str(lives), font=("Arial", 18, "bold"))

def draw_gauge():
    # rub out the old gauge before drawing the new one
    gauge.clear()

    gauge.color("white")
    gauge.goto(60, 310)
    gauge.write("Fuel", font=("Arial", 18, "bold"))

    # green when there's lots of fuel, orange when it's getting low, red when nearly empty
    if fuel > 50:
        gauge.color("lime green")
    elif fuel > 25:
        gauge.color("orange")
    else:
        gauge.color("red")

    # a filled box that is 2 steps wide for every bit of fuel, so 200 wide when full
    gauge.goto(120, 310)
    gauge.begin_fill()
    gauge.goto(120 + fuel * 2, 310)
    gauge.goto(120 + fuel * 2, 330)
    gauge.goto(120, 330)
    gauge.goto(120, 310)
    gauge.end_fill()

    # a white outline that shows how big a full tank is
    gauge.color("white")
    gauge.pendown()
    gauge.goto(320, 310)
    gauge.goto(320, 330)
    gauge.goto(120, 330)
    gauge.goto(120, 310)
    gauge.penup()

# the keys don't move the player, they just say which way to go,
# and swap the picture so the ship leans the way it's moving
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
    # score, lives, fall_speed and fuel are numbers we change, so we need global to change the ones at the top
    global score, lives, fall_speed, fuel

    # stop at the edge of the screen
    if player.direction == -1 and player.xcor() > -300:
        player.setx(player.xcor() - 10)
    if player.direction == 1 and player.xcor() < 300:
        player.setx(player.xcor() + 10)

    # the ship uses up a little fuel every time the game loop runs
    fuel = fuel - 0.2

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

    for cell in fuel_cells:
        cell.sety(cell.ycor() - fall_speed)

        # collected it! top up the tank and send the fuel cell back to the top
        if cell.distance(player) < 25:
            fuel = fuel + 20
            # the tank can't hold more than 100
            if fuel > 100:
                fuel = 100
            cell.goto(random.randint(-300, 300), 350)

        elif cell.ycor() < -350:
            cell.goto(random.randint(-300, 300), 350)

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

    # the tank can't have less than nothing in it
    if fuel < 0:
        fuel = 0

    draw_gauge()
    screen.update()

    # no lives or no fuel left: write GAME OVER and don't run the game loop again
    if lives == 0 or fuel == 0:
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
