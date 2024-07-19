import os
import platform

def clear_console():
    if platform.system() == 'Windows':
        os.system('cls')                      #   not clearing terminal or  output screen :
    else:
        os.system('clear')
from hammer import logo
print(logo)

bid =  {}
bidding_finished = False

def find_highest_bidder(bidding_records):
    highest_bid = 0
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if bid_amount >highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid} ")
while not bidding_finished:
    name = input("What's   your name:")
    price =int(input("What's your bid? $ "))
    bid[name]= price
    should_continue =input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue =="no":
        bidding_finished =True
        find_highest_bidder(bid)
    elif should_continue =="yes":
        clear_console()

