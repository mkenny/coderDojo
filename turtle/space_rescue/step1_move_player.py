# Space Rescue - Step 1: Move the player
#
# New in this step:
# - a player at the bottom of the screen
# - move_left() and move_right() move the player 20 steps when you press an arrow key
# - the player stops at the edges of the screen
# - screen.listen() and onkeypress() connect the arrow keys to the functions

import turtle

screen = turtle.Screen()
screen.title("Space Rescue - Step 1")
screen.setup(700, 700)

player = turtle.Turtle()
player.shape("square")
player.penup()
player.goto(0, -300)

def move_left():
    # stop at the edge of the screen
    if player.xcor() > -300:
        player.setx(player.xcor() - 20)

def move_right():
    if player.xcor() < 300:
        player.setx(player.xcor() + 20)

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

turtle.done()
