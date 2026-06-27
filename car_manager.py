COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars=[]
        self.carspeed=STARTING_MOVE_DISTANCE
            

    def create_car(self):
        self.hideturtle()
        random_chance=random.randint(1,6)
        if random_chance==1:
            car=Turtle("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            rand_y=random.randint(-250,250)
            car.goto(300,rand_y)
            self.cars.append(car)
            

    def move(self):
        for car in self.cars:
            car.backward(self.carspeed)
    
    def level_up(self):
        self.carspeed+=MOVE_INCREMENT


