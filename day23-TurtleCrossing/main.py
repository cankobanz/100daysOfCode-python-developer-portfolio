import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = []
for _ in range(0, 40):
    cars.append(CarManager())

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for i in range(0, 40):
        cars[i].move()
        # Collision detect
        if player.distance(cars[i]) < 20:
            game_is_on = False

    # Detection of win
    if player.check_win():
        scoreboard.increase_level()

scoreboard.game_over()

screen.exitonclick()
