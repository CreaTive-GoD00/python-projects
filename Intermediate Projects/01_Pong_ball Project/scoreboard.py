from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.color("white")
        self.penup()

        self.left_score = 0
        self.right_score = 0

        self.score_update()

    def score_update(self):
        self.clear()

        self.goto(-100, 190)
        self.write(
            self.left_score,
            align="center",
            font=("Courier", 80, "normal")
        )

        self.goto(100, 190)
        self.write(
            self.right_score,
            align="center",
            font=("Courier", 80, "normal")
        )

    def right_update(self):
        self.right_score += 1
        self.score_update()

    def left_update(self):
        self.left_score += 1
        self.score_update()