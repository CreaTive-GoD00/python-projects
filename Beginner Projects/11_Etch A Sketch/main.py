import turtle as t

turtle = t.Turtle()
screen = t.Screen()

turtle.speed("fast")


def move_forward():
    turtle.forward(20)


def move_backward():
    turtle.backward(15)


def turn_right():
    angle = turtle.heading()
    angle -= 10
    turtle.setheading(angle)


def turn_left():
    angle = turtle.heading()
    angle += 10
    turtle.setheading(angle)


def clear():
    turtle.reset()


screen.listen()

screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()