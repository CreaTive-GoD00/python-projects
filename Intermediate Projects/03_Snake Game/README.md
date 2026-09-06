# Snake Game

A classic Snake game built using Python's Turtle graphics module.

The player controls a growing snake, collects food to increase the score, and tries to avoid hitting the walls or the snake's own tail.

The highest score is stored in a local file so it remains available between game sessions.

## Controls

- `Up Arrow` - Move up
- `Down Arrow` - Move down
- `Left Arrow` - Move left
- `Right Arrow` - Move right

The snake cannot immediately reverse into itself.

## Concepts Practiced

- Object-Oriented Programming
- Classes
- Multiple Python modules
- Turtle graphics
- Keyboard event handling
- Game loops
- Collision detection
- Lists of objects
- Dynamic snake growth
- File reading and writing
- Persistent high scores
- Game state and reset logic

## How the Game Works

The snake moves continuously around the screen.

When the snake eats food:

- The food moves to a new random position
- The snake grows by one segment
- The player's score increases

If the snake hits a wall or its own tail:

- The current score is compared with the high score
- A new high score is saved to `data.txt` when necessary
- The snake resets to its starting position
- The player can continue playing

## Project Structure

```text
snake-game/
├── main.py
├── snake.py
├── food.py
├── scoreboard.py
├── data.txt
└── README.md
```

## How to Run

```bash
python main.py
```

A Turtle graphics window will open.

Use the arrow keys to control the snake, collect food, and try to beat the saved high score.