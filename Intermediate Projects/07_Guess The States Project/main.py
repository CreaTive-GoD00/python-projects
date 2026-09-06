import turtle
from turtle import Turtle

import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

background = Turtle()
background.shape(image)

writer = Turtle()
writer.penup()
writer.hideturtle()

data = pd.read_csv("50_states.csv")
states = data["state"].to_list()

correct_states = 0
answers = []

game_on = True


while game_on:
    answer_state = screen.textinput(
        title=f"Guess the States! {correct_states}/50",
        prompt="Enter a U.S. state or type 'Exit':"
    )

    if answer_state is None:
        break

    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [
            state
            for state in states
            if state not in answers
        ]

        missing_data = pd.DataFrame(
            missing_states,
            columns=["State"]
        )

        missing_data.to_csv(
            "states_to_learn.csv",
            index=False
        )

        break

    for state in states:
        if state == answer_state and answer_state not in answers:
            new_x = data.x[data.state == state].item()
            new_y = data.y[data.state == state].item()

            answers.append(answer_state)
            correct_states += 1

            writer.goto(new_x, new_y)
            writer.write(
                state,
                align="center",
                font=("Arial", 10, "bold")
            )