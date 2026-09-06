# Higher Lower Game

A command-line Higher Lower game built while practicing Python functions, dictionaries, imports, and game loops.

The player is shown two public figures and has to guess which one has more followers. Each correct answer increases the score, while one wrong answer ends the game.

## Concepts Practiced

- Functions
- Dictionaries
- Importing data from another Python file
- Random selection
- `while` loops
- Conditional logic
- User input
- Comparing values
- Score tracking
- Basic game state

## How the Game Works

Each round:

- Two random entries are selected from the game data
- The player is shown their name, country, and description
- The player chooses `A` or `B`
- The program compares their follower counts
- A correct answer increases the score
- An incorrect answer ends the game
- The final score is displayed

The program also prevents the same character from appearing on both sides of a round.

## How to Run

```bash
python main.py
```

Make sure the following files are in the same folder:

- `main.py`
- `art.py`
- `game_data.py`

Then follow the prompts in the terminal and try to build the highest score possible.