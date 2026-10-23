import turtle

t = turtle.Turtle()

# each step goes a bit further than the last, so the shape spirals outwards
for i in range(100):
    t.forward(i * 2)
    t.left(90)

turtle.done()
