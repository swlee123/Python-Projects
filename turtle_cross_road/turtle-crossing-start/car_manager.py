COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.setheading(180)
        self.setposition(random.randint(-300, 300), random.randint(-270, 300))


    def move(self):
        self.forward(10)

    def new_car(self):
        self.setx(310)



