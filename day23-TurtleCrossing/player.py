from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 100
FINISH_LINE_Y = 280
STARTING_HEAD = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(STARTING_HEAD)
        self.setposition(STARTING_POSITION)
        self.shape("turtle")
        self.color("black")

    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def check_win(self):
        if self.ycor() > FINISH_LINE_Y:
            self.setposition(STARTING_POSITION)
            return True
        else:
            return False


