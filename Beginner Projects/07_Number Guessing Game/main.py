import random
import art

print("Welcome To The Number Guessing Game!")
print(art.logo)

choice = input(
    "Choose your difficulty: 'easy' or 'hard'\n"
).lower().strip()

if choice == "easy":
    max_number = 50
    attempts = 7
    score_multiplier = 125

elif choice == "hard":
    max_number = 100
    attempts = 9
    score_multiplier = 175

else:
    print("Please enter a valid difficulty!")
    attempts = 0
    max_number = 0
    score_multiplier = 0

if attempts > 0:
    number = random.choice(range(1, max_number + 1))

    print(
        f"\nYou are guessing a number between 1 and {max_number}."
    )
    print(f"You have {attempts} attempts. Good luck! 🫡")

    guessed_correctly = False

    while attempts != 0 and not guessed_correctly:
        print(f"\nYou have {attempts} attempts remaining.")

        guess = int(input("Guess a number:\n"))

        if guess > number:
            print("Too High!")
            attempts -= 1

        elif guess < number:
            print("Too Low!")
            attempts -= 1

        else:
            print("You guessed the correct number! 🎉")
            guessed_correctly = True

    if guessed_correctly:
        score = attempts * score_multiplier
        print(f"Your score is: {score}")

    else:
        print(f"\nYou ran out of attempts. The number was {number}.")
        print("Better luck next time! 😅")