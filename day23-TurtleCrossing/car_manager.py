from turtle import Turtle
import random as rnd

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(rnd.choice(COLORS))
        self.random_location()

    def random_location(self):
        random_x = rnd.randrange(280, 1000, 100)
        random_y = rnd.randint(-280, 280)
        self.goto(random_x, random_y)

    def move(self):
        self.goto(self.xcor() - STARTING_MOVE_DISTANCE, self.ycor())