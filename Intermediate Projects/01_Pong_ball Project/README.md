# Pong Game

A two-player Pong game built using Python's Turtle graphics module.

The project uses multiple Python files and custom classes to manage the paddles, ball movement, collision detection, scoring, and keyboard controls.

## Controls

### Left Player

- `W` - Move paddle up
- `S` - Move paddle down

### Right Player

- `Up Arrow` - Move paddle up
- `Down Arrow` - Move paddle down

## Concepts Practiced

- Object-Oriented Programming
- Classes
- Inheritance
- Multiple Python modules
- Turtle graphics
- Keyboard event handling
- Game loops
- Collision detection
- Object interaction
- Score tracking
- Instance attributes and methods
- Basic game state management

## How the Game Works

The game creates two paddles and a moving ball.

The ball:

- Moves continuously across the screen
- Bounces when it hits the top or bottom wall
- Changes direction when it hits a paddle
- Speeds up slightly after paddle collisions
- Resets to the center after a player scores

The scoreboard keeps track of both players' scores throughout the game.

## Project Structure

```text
pong-game/
├── main.py
├── ball.py
├── paddle.py
├── scoreboard.py
└── README.md
```

## How to Run

```bash
python main.py
```

A Turtle graphics window will open and the game will begin.

Two players can control the paddles from the same keyboard.