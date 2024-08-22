from turtle import Turtle
from cars import cars


class OurTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.seth(90)
        self.penup()
        self.initial_position()

    def initial_position(self):
        self.goto(0, -280)

    def move_forward(self):
        self.forward(2.5)

    def crash(self):
        for i in cars:
            if self.distance(i) < 25:
                return True
