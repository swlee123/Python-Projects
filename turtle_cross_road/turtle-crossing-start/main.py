import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

CAR_NUM = 20
SPEED = 0.12

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
score = Scoreboard()
screen.onkeypress(player.move, "Up")

game_is_on = True
cars = []

def initiate_cars():
    for x in range(CAR_NUM):
        car = CarManager()
        cars.append(car)

def cars_move():
    for x in range(CAR_NUM):
        cars[x].move()

def new_cars():
    more_car = CarManager()
    more_car.new_car()
    cars.append(more_car)

initiate_cars()

while game_is_on:
    score.print_score()

    cars_move()

    for x in cars:

        # if player collide with cars
        if x.distance(player) < 25:
            game_is_on = False
            score.game_over()


        # if car disappear at left side
        if x.xcor() < -320:
            cars.remove(x)
            new_cars()

    if player.ycor() > 300:
        player.reset()
        SPEED -= 0.02
        score.add_score()
        score.print_score()

    time.sleep(SPEED)
    screen.update()



screen.exitonclick()