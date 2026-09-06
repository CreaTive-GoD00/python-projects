# Coffee Machine

A command-line coffee machine simulator built while practicing Python functions, dictionaries, loops, and resource management.

The program allows a user to choose a drink, insert coins, receive change, and order coffee while the machine keeps track of its available ingredients and profit.

## Menu

The machine can prepare:

- Espresso - $1.50
- Latte - $2.50
- Cappuccino - $3.00

It also supports additional commands:

- `menu` - display the available drinks
- `report` - display the remaining resources and current profit
- `off` - turn off the machine

## Concepts Practiced

- Functions
- Function parameters and return values
- Nested dictionaries
- `while` loops
- `for` loops
- Conditional logic
- User input
- Resource tracking
- Money calculations
- Updating dictionary values
- Basic program state

## How the Program Works

When a drink is selected, the program:

1. Checks whether enough ingredients are available
2. Asks the user to insert coins
3. Calculates the total amount inserted
4. Checks whether enough money was provided
5. Returns change when necessary
6. Deducts the required ingredients
7. Adds the drink price to the machine's profit
8. Serves the selected coffee

The machine continues accepting orders until the `off` command is entered.

## How to Run

```bash
python main.py
```

Turn on the machine and choose one of the available drinks or commands from the terminal menu.