import turtle

t = turtle.Turtle()

l = int(input("Enter the length:"))
w = int(input("Enter the width:"))

# a rectangle is the same two sides drawn twice: length, turn, width, turn
for i in range(2):
    t.forward(l)
    t.left(90)
    t.forward(w)
    t.left(90)

turtle.done()
