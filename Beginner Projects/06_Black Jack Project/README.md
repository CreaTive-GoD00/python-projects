# Blackjack

A command-line Blackjack game built while learning Python functions, loops, and game logic.

The player competes against a computer dealer and tries to get as close to 21 as possible without going over.

This project was completed as part of the **100 Days of Code** course and was based on the course-guided Blackjack implementation. I later customized the program with my own menu, game instructions, wording, and interaction flow after my original version was lost.

## Features

- Play Blackjack against a computer dealer
- Random card dealing
- Blackjack detection
- Ace handling as either 11 or 1
- Dealer automatically draws until reaching at least 17
- Game result comparison
- Built-in rules/manual
- Option to play multiple games or exit

## Concepts Practiced

- Functions
- Function parameters and return values
- Lists
- `while` loops
- `for` loops
- Conditional logic
- Random selection
- Game state
- User input
- Basic program organization

## How to Play

The goal is to get a hand value as close to **21** as possible without exceeding it.

- Number cards use their normal value
- Jack, Queen and King are worth `10`
- Ace can count as `11` or `1`
- A starting hand worth exactly `21` is Blackjack
- The dealer continues drawing until reaching at least `17`
- The highest valid score wins

## How to Run

```bash
python main.py
```

From the main menu, choose:

- `play` to start a game
- `manual` to view the rules
- `exit` to close the program

Make sure the following files are in the same folder:

- `main.py`
- `art.py`