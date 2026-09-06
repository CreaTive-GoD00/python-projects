import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_MOVE_DISTANCE = 20


class CarManager:

    def __init__(self):
        self.cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)

        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))

            car.shapesize(
                stretch_wid=1,
                stretch_len=random.randint(2, 3)
            )

            new_x = random.randint(280, 295)
            new_y = random.randint(-260, 260)

            car.goto(new_x, new_y)

            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            new_x = car.xcor() - CAR_MOVE_DISTANCE
            car.goto(new_x, car.ycor())

    def remove_old_cars(self):
        for car in self.cars[:]:
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)