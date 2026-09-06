# U.S. States Game

An interactive geography game built using Python, Turtle graphics, and Pandas.

The player tries to name all 50 U.S. states. Correct answers are written onto the map at their corresponding coordinates.

If the player exits before completing the game, the missing states are saved to a CSV file for later study.

## Concepts Practiced

- Turtle graphics
- Pandas
- Reading CSV files
- DataFrames
- Converting columns to lists
- Filtering DataFrame values
- List comprehensions
- User input
- Tracking game progress
- Coordinate-based drawing
- Writing generated CSV files

## How the Game Works

The program displays a blank map of the United States.

The player enters the name of a state.

If the answer is correct:

- The state is added to the list of correct answers
- The score increases
- The state's name is written at its location on the map

The game continues until the player exits or identifies all states.

## Learning File

If the player types:

```text
Exit
```

the program compares the guessed states with the complete list of states.

Any states that were not guessed are saved to:

```text
states_to_learn.csv
```

This creates a personalized list of states to review.

## Project Structure

```text
us-states-game/
├── main.py
├── 50_states.csv
├── blank_states_img.gif
└── README.md
```

## How to Run

```bash
python main.py
```

Make sure `50_states.csv` and `blank_states_img.gif` are located in the same folder as `main.py`.