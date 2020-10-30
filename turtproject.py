# turtle syntax

# to make square

import turtle

my_turtle = turtle.Turtle()

my_turtle.forward(100)

my_turtle.right(90)

my_turtle.forward(100)

my_turtle.right(90)

my_turtle.forward(100)

my_turtle.right(90)

my_turtle.forward(100)

# to make circle

r = 50

my_turtle.circle(r)

# to make various circles

r = 50

n = 10

for i in range(1, n + 1, 1):

    my_turtle.circle(r * i)
