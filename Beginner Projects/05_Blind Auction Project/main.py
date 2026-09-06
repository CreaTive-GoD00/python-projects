import art

print(art.logo)

print("Welcome to the Secret Auction!")

ready = input("Are you here to place a bid? Type 'yes' or 'no':\n").lower()

if ready == "no":
    print("Alright, you may leave the auction. 👋")

else:
    item = input("What are you bidding for?\n")

    print(f"\nThe bidding for {item.upper()} has started!")

    bidding = 1
    bids = {}

    while bidding == 1:
        name = input("\nEnter your name:\n")
        bid = int(input("Enter your bid:\n₹"))

        bids[name] = bid

        bidders = input(
            "Are there any other bidders? Type 'yes' or 'no':\n"
        ).lower()

        if bidders == "yes":
            print("\n" * 50)
            bidding = 1
        else:
            bidding = 0

    highest_bid = 0
    winner = ""

    for name in bids:
        if bids[name] > highest_bid:
            highest_bid = bids[name]
            winner = name

    print(
        f"\nThe winner of the bidding for {item.upper()} is "
        f"{winner.upper()} with a bid of ₹{highest_bid}!"
    )