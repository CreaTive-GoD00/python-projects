# Squirrel Census Analysis

A small Pandas project using data from the Central Park Squirrel Census.

The program reads a CSV dataset, counts squirrels based on their primary fur color, creates a summary DataFrame, and exports the results to a new CSV file.

## Concepts Practiced

- `pandas.read_csv()`
- DataFrame filtering
- Boolean conditions
- Counting rows
- Dictionaries
- Creating DataFrames
- Exporting CSV files

## How It Works

The program:

1. Loads the squirrel census CSV file
2. Filters squirrels by primary fur color
3. Counts Gray, Black, and Cinnamon squirrels
4. Stores the results in a new DataFrame
5. Exports the summary to `squirrel_count.csv`

## How to Run

```bash
python main.py
```

Make sure the squirrel census CSV file is in the same folder as `main.py`.