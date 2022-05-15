#Python Turtle Graphics - https://docs.python.org/3/library/turtle.html

import turtle as t
import random

#defines the degrees and colours used in the turtle
degrees = [0, 90, 180, 270]
colours = ["lavender", "medium purple", "slate blue", "dark slate blue"]

turt = t.Turtle()
for _ in range(200):
    #this code tells the turtle where to move and randomises 
    directions =[turt.right, turt.left]
    set_direction = random.choice(directions)
    set_direction(random.choice(degrees))
    turt.color(random.choice(colours))

    # personalises the turtle and screen. incl the thickness of the turtle's drawing +speed
    screen = t.bgcolor("dim grey")
    screen = t.screensize(100,100)
    screen = t.title("Welcome to the randomised turtle")
    turt.shape("turtle")
    turt.pensize(10)
    turt.speed(20)
    turt.forward(30)


#loads screen
screen = t.screen()
screen = t.exitonclick