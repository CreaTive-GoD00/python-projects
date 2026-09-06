import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game 🐍")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Food collision
    if snake.head.distance(food) < 17:
        food.refresh()
        scoreboard.score_add()
        snake.snake_grow()

    # Wall collision
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        scoreboard.reset_game()
        snake.snake_reset()

    # Tail collision
    elif snake.tail_collide():
        scoreboard.reset_game()
        snake.snake_reset()


screen.exitonclick()