#Random objects
#
#---------------
from shapeclasses import *
from time import sleep
import random
t = turtle.Turtle()

screen = turtle.Screen()
screen.setup(900, 700)

turtle.tracer(0)
shapes = ["square","circle","triangle"]

colours = ["red","green","yellow","blue"]

triangle_sizes = [(50,70,40),(30,40,50),(50,70,90)]

def triangle_create():
    sides = random.choice(triangle_sizes)
    
    return Triangle(colour = random.choice(colours) ,is_filled = False, side_a = sides[0],side_b = sides[1],side_c = sides[2],turtle_obj = t)

def square_create():
    return Square(colour = random.choice(colours),is_filled = True, width = random.randint(30,80),turtle_obj = t)

def circle_create():
    return Circle(colour = random.choice(colours),is_filled = True, radius = random.randint(10,40), turtle_obj = t)


def move_position():
    x = random.randint(-400,400)
    y = random.randint(-300,300)
    t.penup()
    t.goto(x,y)
    t.pendown()

while True:
    for x in range(random.randint(40,60)):
        match random.choice(shapes):
            case "square":
                move_position()
                square_create().draw()
            case "triangle":
                move_position()
                triangle_create().draw()
            case "circle":
                move_position()
                circle_create().draw()
    sleep(0.5)
    t.reset() 
        
        