import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager=CarManager()
player=Player()
score=Scoreboard()
screen.listen()
screen.onkeypress(player.go_up,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    #DETECT COLLISON WITH CAR
    for car in car_manager.cars:
        if car.distance(player)<20:
            score.game_over()
            game_is_on=False
    #DETECT A SUCCESSFULL CROSSING
    if player.ycor()>280:
        player.reset()
        car_manager.level_up()
        score.inc_level()


screen.exitonclick()
    
