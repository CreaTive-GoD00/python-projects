# Password Manager

A desktop password manager built using Python's Tkinter library.

The application allows the user to save website login details, generate random passwords, copy generated passwords to the clipboard, and search previously saved credentials.

Data is stored locally using JSON.

## Features

- Website, email, and password input fields
- Random password generation
- Automatic clipboard copying
- JSON-based local storage
- Search for saved website credentials
- Basic input validation
- File handling
- Error handling for missing data files
- Tkinter graphical interface

## Concepts Practiced

- Tkinter
- GUI layouts
- Entry fields
- Buttons and labels
- Callback functions
- Random password generation
- Lists and list comprehensions
- `shuffle()`
- JSON
- File reading and writing
- Dictionaries
- Updating stored data
- `try` / `except`
- `else`
- `finally`
- Message boxes
- Clipboard interaction with `pyperclip`

## How It Works

The user enters:

- Website name
- Email or username
- Password

A password can also be generated using the `Generate Password` button.

The generated password is:

1. Created using random letters, numbers, and symbols
2. Inserted into the password field
3. Automatically copied to the clipboard

When the `Add` button is pressed, the details are saved to `data.json`.

If the file does not exist yet, the program creates it automatically.

The `Search` button can be used to retrieve previously saved credentials for a website.

## Project Structure

```text
password-manager/
├── main.py
├── logo.png
└── README.md
```

The `data.json` file is created automatically when data is saved.

## Requirements

This project uses the `pyperclip` package.

Install it using:

```bash
pip install pyperclip
```

## How to Run

```bash
python main.py
```

Make sure `logo.png` is located in the same folder as `main.py`.

## Security Note

This project was created as a Python learning exercise.

Passwords are stored locally in plain text inside a JSON file, so the application should not be used for storing real or sensitive credentials.

A production password manager would require secure encryption and stronger credential-handling practices.