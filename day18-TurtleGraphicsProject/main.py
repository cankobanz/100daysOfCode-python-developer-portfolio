import colorgram as cg
import random
import turtle as t
from turtle import Turtle, Screen

# colors = [tuple(color.rgb) for color in cg.extract("image.jpg", 30)]
colors = [(246, 243, 239), (247, 241, 244), (202, 166, 109), (240, 246, 241), (152, 73, 47), (236, 238, 244),
          (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71),
          (16, 97, 75), (100, 73, 75), (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50),
          (130, 28, 31), (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83),
          (215, 177, 182), (19, 71, 63), (175, 192, 212)]

mc_mikey = Turtle()
mc_mikey.shape("arrow")
mc_mikey.color("orange")
mc_mikey.speed(0)
mc_mikey.hideturtle()
t.colormode(255)


def draw_dot():
    mc_mikey.dot(20, random.choice(colors))


def art_generator(width=10, height=10):
    mc_mikey.penup()
    pos_x = -width*50/2
    pos_y = -height*50/2
    mc_mikey.setposition(pos_x, pos_y)
    for w in range(width):
        pos_y += 50
        mc_mikey.setposition(pos_x, pos_y)
        for h in range(height):
            mc_mikey.setheading(0)
            mc_mikey.forward(50)
            draw_dot()


art_generator()
screen = Screen()
screen.exitonclick()
