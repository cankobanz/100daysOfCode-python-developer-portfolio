from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_move = 10
        self.x_move = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def collide_wall(self):
        self.y_move *= -1

    def collide_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto((0, 0))
        self.x_move *= -1
