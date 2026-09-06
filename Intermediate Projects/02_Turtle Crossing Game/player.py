from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)

        self.go_to_start()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def backward(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def go_to_start(self):
        self.goto(STARTING_POSITION)