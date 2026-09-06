from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.penup()

        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)

        self.goto(pos_x, pos_y)

    def up(self):
        self.forward(25)

    def down(self):
        self.backward(25)