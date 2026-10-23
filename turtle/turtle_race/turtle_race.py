import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light green")
screen.setup(800, 600)

writer = turtle.Turtle()
writer.hideturtle()

colours = ["red", "green", "blue", "pink", "yellow"]

bet = screen.textinput("Who will win? ", colours)

def make_racer(colour, y):
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.color(colour)
    racer.penup()
    racer.goto(-300, y)
    return racer

def make_powerup(y):
    # start hidden so it doesn't flash up in the middle of the track
    powerup = turtle.Turtle(visible=False)
    powerup.shape("circle")
    powerup.shapesize(0.5)
    # gold speeds a turtle up, black slows it down
    powerup.color(random.choice(["gold", "black"]))
    # powerup.speed(0)
    powerup.penup()
    powerup.goto(random.randint(-200, 250), y)
    powerup.showturtle()
    return powerup

def draw_finishline():
    finishLine = turtle.Turtle()
    finishLine.hideturtle()
    finishLine.penup()
    finishLine.goto(300, -150)
    finishLine.pendown()
    finishLine.goto(300, 150)

draw_finishline()

y = 120
racers = []
powerups = []
for colour in colours:
    racers.append(make_racer(colour, y))
    y = y-60

winner = False
winningRacer = ""
while winner == False:
    # sometimes a new powerup appears in a random racer's lane
    if random.randint(1, 15) == 1:
        lane = random.choice(racers).ycor()
        powerups.append(make_powerup(lane))

    # sometimes a powerup disappears before anyone gets it
    for powerup in powerups[:]:
        if random.randint(1, 40) == 1:
            powerup.hideturtle()
            powerups.remove(powerup)

    for racer in racers:
        racer.forward(random.randint(1,10))

        # did this racer land on a powerup? used ones are removed from the list
        # loop over a copy ([:]) so removing from powerups is safe
        for powerup in powerups[:]:
            if racer.distance(powerup) < 10:
                if powerup.pencolor() == "gold":
                    racer.forward(50)
                else:
                    racer.backward(50)
                powerup.hideturtle()
                powerups.remove(powerup)

        if racer.xcor() >= 300:
            winningRacer = racer.pencolor()
            winner = True
            break


if bet == winningRacer:
    message = "You're a winner " + winningRacer + " finished first!"
else:
    message = "You lose " + winningRacer + " won and you bet " + bet

writer.write(message, align="center", font=("Arial", 24, "bold"))

turtle.done()