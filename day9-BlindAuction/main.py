from os import system
from art import logo

print(logo)
breakCond = True
bidders = {}
highestBidderName = ""
highestBid = 0
while breakCond:
    name = input("What is your name?: ")

    bid = input("What is your bid?: $")
    if bid.isdigit():
        bid = int(bid)
        bidders[name] = bid
    else:
        print("Please enter a digit for bid.")
        continue

    anyBidders = input("Are there any bidders? Type 'yes' or 'no'.\n")

    if anyBidders == "no":
        breakCond = False
        for bidder in bidders:
            if bidders[bidder] > highestBid:
                highestBidderName = bidder
                highestBid = bidders[bidder]
        print(f"The winner is {highestBidderName} with amount {highestBid}")
    elif anyBidders == "yes":
        system('cls')
        continue
    else:
        print("Please, type 'yes' or 'no'.")
