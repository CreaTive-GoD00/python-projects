import turtle as t
import random

turtle = t.Turtle()
screen = t.Screen()

t.colormode(255)

turtle.speed("fastest")
turtle.shape("turtle")

color_list = [
    (202, 164, 110),
    (236, 239, 243),
    (149, 75, 50),
    (222, 201, 136),
    (53, 93, 123),
    (170, 154, 41),
    (138, 31, 20),
    (134, 163, 184),
    (197, 92, 73),
    (47, 121, 86),
    (73, 43, 35),
    (145, 178, 149),
    (14, 98, 70),
    (232, 176, 165),
    (160, 142, 158),
    (54, 45, 50),
    (101, 75, 77),
    (183, 205, 171),
    (36, 60, 74),
    (19, 86, 89),
    (82, 148, 129),
    (147, 17, 19),
    (27, 68, 102),
    (12, 70, 64),
    (107, 127, 153),
    (176, 192, 208),
    (168, 99, 102),
]


def goto_start():
    turtle.penup()
    turtle.setheading(225)
    turtle.forward(300)
    turtle.setheading(360)


def line():
    for _ in range(9):
        turtle.color(random.choice(color_list))
        turtle.dot(30)
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
        turtle.dot(30)


def left_turn():
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(50)
    turtle.setheading(180)


def right_turn():
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(50)
    turtle.setheading(360)


goto_start()

for _ in range(5):
    line()
    left_turn()
    line()
    right_turn()

screen.exitonclick()