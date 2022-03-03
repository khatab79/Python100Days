from replit import clear
from art import logo


continue_auction = "yes"

def secret_auction_winner( bidders ):

    highest_bid = 0
    for bidder in bidders:
        if bidders[bidder] > highest_bid:
            
            highest_bid = bidders[bidder]  
            winner = bidder
        
    print("The winner is {}, with a bid of ${}".format(winner, highest_bid))
    
clear()
print(logo)

bidders = {}

while continue_auction == "yes":
    name = input("what is your name? ")
    bid  = float(input("what is your bid price ? $"))

    bidders[name] = bid
    
    continue_auction = input("is there any one want to bid ? \n").lower()
    clear()
secret_auction_winner(bidders)