import turtle
 
t = turtle.Turtle()

l = int(input("Enter the length:"))
w = int(input("Enter the width:"))

# drawing first side
t.forward(l) 
t.left(90) 

# drawing second side
t.forward(w) 
t.left(90) 

# drawing third side
t.forward(l) 
t.left(90) 

# drawing fourth side
t.forward(w)
t.left(90)

turtle.done()