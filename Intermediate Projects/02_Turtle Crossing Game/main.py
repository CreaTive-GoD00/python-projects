import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")
screen.onkeypress(player.backward, "Down")
screen.onkeypress(player.left, "Left")
screen.onkeypress(player.right, "Right")

level_speed = 0.1
game_is_on = True


while game_is_on:
    time.sleep(level_speed)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    car_manager.remove_old_cars()

    # Player reaches the finish line
    if player.ycor() > 270:
        player.go_to_start()
        scoreboard.increase_level()

        level_speed *= 0.9

    # Collision with a car
    for car in car_manager.cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            player.hideturtle()
            game_is_on = False


screen.exitonclick()