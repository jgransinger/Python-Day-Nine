# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)

bid_tracker = {}
other_bidders = "y"
max_bid = 0
max_bidder = ""

while other_bidders == "y":
    name = input("What is your name?: ").upper()
    bid = int(input("What is your bid?: "))
    other_bidders = input("Are there other bidders? y/n: ").lower()
    bid_tracker.update({name:bid})

    if bid > max_bid:
        max_bid = bid
        max_bidder = name

    if other_bidders == "n":
        print(f"\n*****************************************\n"
              f"{max_bidder} is the winner with a bid of ${max_bid}\n"
              f"*****************************************\n")
    else:
        print("\n" * 25)

# print(bid_tracker)
