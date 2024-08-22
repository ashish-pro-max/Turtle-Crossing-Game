from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.goto(-270, 245)
        self.ht()
        self.write(arg=f"Level : {self.level}", font=("COURIER", 25, "normal"))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level : {self.level}", font=("COURIER", 25, "normal"))

    def game_over(self):
        self.goto(-63, 0)
        self.write(arg="GAME OVER", font=("COURIER", 15, "bold"))
