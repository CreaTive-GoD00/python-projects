from turtle import Turtle


ALIGN = "center"
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0

        try:
            with open("data.txt", "r") as data:
                self.high_score = int(data.read())
        except FileNotFoundError:
            self.high_score = 0

            with open("data.txt", "w") as data:
                data.write("0")

        self.color("white")
        self.penup()
        self.hideturtle()

        self.goto(0, 270)

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()

        self.write(
            f"Score: {self.score}   High Score: {self.high_score}",
            align=ALIGN,
            font=FONT
        )

    def score_add(self):
        self.score += 125
        self.update_scoreboard()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", "w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()