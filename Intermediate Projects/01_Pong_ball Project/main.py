import time
from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Paddle(340, 0)
left_paddle = Paddle(-340, 0)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

game_on = True

while game_on:
    time.sleep(ball.ball_speed)

    screen.update()
    ball.move()

    # Bounce from top and bottom walls
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.y_bounce()

    # Bounce from paddles
    if (
        ball.distance(right_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(left_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.x_bounce()

    # Left player scores
    if ball.xcor() > 380:
        scoreboard.left_update()
        ball.reset_pos()

    # Right player scores
    elif ball.xcor() < -380:
        scoreboard.right_update()
        ball.reset_pos()

screen.exitonclick()