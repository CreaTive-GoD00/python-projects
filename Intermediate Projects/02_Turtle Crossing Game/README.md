# Turtle Crossing Game

A Turtle Crossing game built using Python's Turtle graphics module.

The player controls a turtle and tries to cross a road filled with randomly generated moving cars. Each successful crossing increases the level and makes the game progressively faster.

## Controls

- `Up Arrow` - Move forward
- `Down Arrow` - Move backward
- `Left Arrow` - Move left
- `Right Arrow` - Move right

## Concepts Practiced

- Object-Oriented Programming
- Classes
- Inheritance
- Multiple Python modules
- Turtle graphics
- Keyboard event handling
- Game loops
- Collision detection
- Random object generation
- Lists of objects
- Game state
- Level tracking
- Increasing game difficulty

## How the Game Works

The player starts at the bottom of the screen and must reach the opposite side of the road.

Cars are randomly generated and move across the screen.

When the player successfully reaches the finish line:

- The turtle returns to the starting position
- The level increases
- The game becomes faster

If the turtle collides with a car, the game ends and `GAME OVER` is displayed.

## Project Structure

```text
turtle-crossing/
├── main.py
├── player.py
├── car_manager.py
├── scoreboard.py
└── README.md
```

## How to Run

```bash
python main.py
```

A Turtle graphics window will open.

Use the arrow keys to guide the turtle across the road while avoiding the moving cars.