import random
import art
import game_data


def character():
    return random.choice(game_data.data)


def compare(a, b):
    if a["followers"] > b["followers"]:
        return "a"
    elif a["followers"] < b["followers"]:
        return "b"


print(art.logo)

score = 0
game_over = False

while not game_over:
    a = character()
    b = character()

    while a == b:
        b = character()

    print(f"A: {a['name']} is a {a['country']} {a['description']}")
    print(art.vs)
    print(f"B: {b['name']} is a {b['country']} {b['description']}")

    choice = input(
        "Who has more followers? Type 'A' or 'B':\n"
    ).lower().strip()

    result = compare(a, b)

    if choice == result:
        score += 1
        print(f"\nCorrect! Your current score is {score}. 🎉\n")

    else:
        game_over = True
        print("\nYou Lose! 😅")
        print(f"Your final score is {score}.")