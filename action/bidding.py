"""
Containing the fields, methods and algorithm pertaining to making a decisions during bidding.

As is: There is no logic. It's a simply roll of the d10 dice to be added on minimum value of share.
To be: Use data to decide to choose a bidding maximum, iteration and style.
"""

from util.tools import ask_user_cait_bid_prompt
from util.tools import roll_dice


def get_bidding_max(share_min):
    result = roll_dice(10)
    return share_min + result


def calculate_caits_bid(current_bid, max_bid):
    """
    TODO: Check if the left side of if statement works
    """

    new_bid = current_bid + (roll_dice(3) - 1)
    return 0 if new_bid == current_bid and new_bid > max_bid else new_bid


def bidding_process(starting_bid):
    bid = starting_bid
    max_bid = get_bidding_max(starting_bid)

    while True:
        caits_bid = calculate_caits_bid(bid, max_bid)
        if caits_bid == 0:
            print("Cait is passing\n")
            break
        else:
            print(f"Cait is bidding £{caits_bid}\n")

        result = ask_user_cait_bid_prompt("Did Cait win or is there a new bid? Y/£ ")
        if type(result) is bool:
            print(f"Cait has won the bid at £{caits_bid}\n")
            break
        else:
            bid = result
