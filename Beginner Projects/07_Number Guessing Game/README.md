# Number Guessing Game

A command-line number guessing game built while practicing Python loops, conditionals, and random number generation.

The player chooses a difficulty level and tries to guess a randomly generated number before running out of attempts.

## Difficulty Levels

### Easy

- Guess a number between `1` and `50`
- 7 attempts
- Each remaining attempt is worth 125 points

### Hard

- Guess a number between `1` and `100`
- 7 attempts
- Each remaining attempt is worth 175 points

## Concepts Practiced

- Random number generation
- `while` loops
- `if / elif / else`
- User input
- Variables
- Comparison operators
- Basic scoring logic
- Tracking remaining attempts

## How the Game Works

The program:

- Asks the player to choose Easy or Hard difficulty
- Generates a random number within the selected range
- Gives feedback when a guess is too high or too low
- Reduces the number of remaining attempts after an incorrect guess
- Ends when the correct number is guessed or all attempts are used
- Calculates a score based on the number of attempts remaining

## How to Run

```bash
python main.py
```

Make sure the following files are in the same folder:

- `main.py`
- `art.py`

Choose a difficulty and follow the prompts in the terminal.