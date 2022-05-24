FONT = ("Courier", 20, "normal")

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("Black")
        self.score = 0
        self.setposition(-250, 250)

    def print_score(self):
        self.clear()
        self.write(f"Score = {self.score}", align="left", font=FONT)

    def add_score(self):
        self.score += 1

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over!", align="center", font=FONT)




