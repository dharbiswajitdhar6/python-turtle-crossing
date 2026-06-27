FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update_level()
        

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left",font=FONT )
    
    def inc_level(self):
        self.level+=1
        self.update_level()

    def game_over(self):
        self.goto(-20,0)
        self.write("Game Over",align="center",font=FONT)  
