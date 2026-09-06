import random
from art import logo


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Calculates and returns the score of a hand."""

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw 🙃"
    elif computer_score == 0:
        return "You lose. The dealer has Blackjack 😱"
    elif user_score == 0:
        return "Blackjack! You win 😎"
    elif user_score > 21:
        return "You went over 21. You lose 😭"
    elif computer_score > 21:
        return "The dealer went over 21. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def show_manual():
    print("\n---------- BLACKJACK MANUAL ----------")
    print("Your goal is to get as close to 21 as possible without going over.")
    print("Number cards are worth their face value.")
    print("Jack, Queen and King are worth 10.")
    print("Ace can count as 11 or 1.")
    print("A starting hand worth exactly 21 is Blackjack.")
    print("You can choose another card or pass.")
    print("The dealer keeps drawing cards until reaching at least 17.")
    print("Whoever has the higher valid score wins.")
    print("--------------------------------------\n")


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []

    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:
            user_should_deal = input(
                "Type 'y' to take another card or 'n' to pass: "
            ).lower()

            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(
        f"Dealer's final hand: {computer_cards}, "
        f"final score: {computer_score}"
    )

    print(compare(user_score, computer_score))


print("Welcome to Blackjack! 🃏")

running = True

while running:
    choice = input(
        "\nType 'play' to start the game, "
        "'manual' to see the rules, or 'exit' to leave:\n"
    ).lower().strip()

    if choice == "play":
        print("\n" * 10)
        play_game()

    elif choice == "manual":
        show_manual()

    elif choice == "exit":
        print("Thanks for stopping by. See you next time! 👋")
        running = False

    else:
        print("Please choose 'play', 'manual', or 'exit'.")