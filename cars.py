from turtle import Turtle
import random

colors = ["pink", "orange", "red", "green", "blue", "yellow", "purple", "brown"]
cars = []


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.color(random.choice(colors))
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(320, random.randint(-230, 230))
        self.seth(180)
        cars.append(self)
        if len(cars) > 27:
            cars[0].ht()
            cars.pop(0)

    def move_cars(self):
        for i in cars:
            i.forward(3)
