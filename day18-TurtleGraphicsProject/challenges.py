import colorsys
import random
import turtle
from turtle import Turtle, Screen

mc_mikey = Turtle()
mc_mikey.shape("arrow")
mc_mikey.color("orange")
mc_mikey.pensize(1)
mc_mikey.speed(0)
turtle.colormode(255)


def draw_dashed_line(distance):
    for i in range(distance):
        mc_mikey.forward(10)
        mc_mikey.penup()
        mc_mikey.forward(10)
        mc_mikey.pendown()


def draw_shape(num_sides):
    for _ in range(num_sides):
        mc_mikey.pen(pencolor=random.choice(colors), pensize=5)
        mc_mikey.forward(100)
        mc_mikey.right(360 / edge)


# edges = [_ for _ in range(3, 11)]
# for edge in edges:
#     draw_shape(edge)
def random_color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_random_walk(duration):
    directions = [0, 90, 180, 270]
    for _ in range(duration):
        mc_mikey.color(random_color_generator())
        mc_mikey.forward(30)
        mc_mikey.setheading(random.choice(directions))


def draw_spirograph(size_of_the_gap):
    degree = 0
    for _ in range(int(360/size_of_the_gap)):
        mc_mikey.color(random_color_generator())
        mc_mikey.circle(radius=100)
        mc_mikey.setheading(degree)
        degree += size_of_the_gap


draw_spirograph(5)
screen = Screen()
screen.exitonclick()
