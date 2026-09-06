import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.color("brown")
        self.speed("fastest")
        self.shapesize(0.8, 0.8)

        self.refresh()

    def refresh(self):
        new_x = random.randint(-270, 270)
        new_y = random.randint(-270, 270)

        self.goto(new_x, new_y)