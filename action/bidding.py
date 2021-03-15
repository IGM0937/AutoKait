"""
Containing the fields, methods and algorithm pertaining to making a decisions during bidding.

As is: There is no logic. It's a simply roll of the d10 dice to be added on minimum value of share.
To be: Use data to decide to choose a bidding maximum, iteration and style.
"""

from util.tools import roll_dice


def get_bidding_max(share_min):
    result = roll_dice(10)
    return share_min + result
