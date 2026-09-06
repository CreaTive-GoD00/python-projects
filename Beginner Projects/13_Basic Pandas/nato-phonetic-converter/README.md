# NATO Phonetic Alphabet Converter

A small Python and Pandas project that converts a word into its NATO phonetic alphabet representation.

The program reads NATO alphabet data from a CSV file, creates a lookup dictionary, and converts each letter entered by the user into its corresponding phonetic code word.

Invalid input is handled using Python exception handling.

## Concepts Practiced

- Pandas
- `pandas.read_csv()`
- DataFrames
- `.iterrows()`
- Dictionary comprehensions
- List comprehensions
- Dictionary lookups
- Functions
- `try` / `except`
- `else` with exception handling
- Handling `KeyError`
- User input

## Example

Input:

```text
CAT
```

Output:

```text
['Charlie', 'Alfa', 'Tango']
```

If the user enters numbers or unsupported characters, the program asks for another word instead of crashing.

## Project Structure

```text
nato-phonetic-converter/
├── main.py
├── nato_phonetic_alphabet.csv
└── README.md
```

## How to Run

```bash
python main.py
```

Make sure `nato_phonetic_alphabet.csv` is located in the same folder as `main.py`.