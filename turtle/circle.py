import turtle

screen = turtle.Screen()
screen.title("Animation Circle")
screen.bgcolor("black")

t = turtle.Turtle()
t.color("yellow")
t.speed(0)
t.hideturtle()

# draw 100 circles, each a bit bigger and turned a bit further than the last
for i in range(100):
    t.circle(i * 2)
    t.left(5)

turtle.done()
