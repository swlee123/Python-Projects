from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        with open("data.txt", mode='r')as file:
            content = file.readline(1)
            if content.isdigit():
                self.high_score = content
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High_Score: {self.high_score} ", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > int(float(self.high_score)):
            self.high_score = self.score
            with open("data.txt", mode='w+')as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()
