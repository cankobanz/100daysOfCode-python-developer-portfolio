from turtle import Turtle, Screen
from snake import Snake
import time

snake = Snake()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Yılaaann")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()





screen.exitonclick()
