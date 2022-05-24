STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.setheading(90)
        self.setposition(STARTING_POSITION)
        self.shape("turtle")

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.setposition(STARTING_POSITION)


