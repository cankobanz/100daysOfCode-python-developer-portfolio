from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_scoreboard = Scoreboard((100, 240))
l_scoreboard = Scoreboard((-100, 240))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    # Detection of collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.collide_wall()

    # Detection of collision with paddle.
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
            (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.collide_paddle()

    # Detection of R paddle misses
    if ball.xcor() > 370:
        ball.reset()
        l_scoreboard.increase_score()

    # Detection of L paddle misses
    if ball.xcor() < -370:
        ball.reset()
        r_scoreboard.increase_score()

screen.exitonclick()
