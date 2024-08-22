from turtle import Screen
from our_turtle import OurTurtle
from cars import Cars
from scoreboard import Score
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.listen()
screen.tracer(0)

timmy = OurTurtle()
car = Cars()
score = Score()

screen.onkeypress(key="w", fun=timmy.move_forward)
screen.onkeypress(key="Up", fun=timmy.move_forward)

game_is_on = True
delay = 0.05

while game_is_on:
    screen.update()
    random_choice = random.randint(1, 11)
    if random_choice == 1:
        car = Cars()
    screen.update()
    car.move_cars()
    time.sleep(delay)

    # Collision with cars
    if timmy.crash():
        score.game_over()
        game_is_on = False
        time.sleep(2)

    # Collision with finish line
    if timmy.ycor() > 240:
        score.increase_level()
        timmy.initial_position()
        delay *= 0.7

# screen.exitonclick()
