from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 32, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=self.score, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
