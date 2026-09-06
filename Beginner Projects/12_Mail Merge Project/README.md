# Mail Merge

A simple Python file-handling project that generates personalized letters for multiple people.

The program reads a letter template and a list of names, replaces the `[name]` placeholder for each person, and saves the personalized letters into an output folder.

## Concepts Practiced

- File reading and writing
- `read()`
- `readlines()`
- `with open()`
- String replacement
- `.strip()`
- Loops
- Creating multiple output files

## How It Works

The program:

1. Reads the letter template from `starting_letter.txt`
2. Reads names from `invited_names.txt`
3. Replaces the `[name]` placeholder with each person's name
4. Creates a separate personalized letter
5. Saves each generated letter inside the `ReadyToSend` folder

## Project Structure

```text
mail-merge/
├── main.py
├── Input/
│   ├── letters/
│   │   └── starting_letter.txt
│   └── Names/
│       └── invited_names.txt
└── Output/
    └── ReadyToSend/
```

## How to Run

```bash
python main.py
```

The generated personalized letters will appear inside:

```text
Output/ReadyToSend/
```