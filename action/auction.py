"""
Containing the fields, methods and algorithm pertaining to making a decision to which company to auction for.

As is: It's purely based on the company with most connections, and decided by the human players.
To be: Use data to decide which company to auction for.
"""

from action.bidding import take_bidding_action
from action.dividends import call_dividends_action
from util.tools import *


def call_auction_action():
    print(output.call_auction_action_text())
    global_vars.last_action = ACTION_CALL_AUCTION
    # TODO: Is there a way to determine if an action can be performed without asking the question?
    if ask_user_yes_no_prompt(output.call_auction_action_be_performed_text()):
        take_bidding_action(True)
    else:
        print(output.cait_turn_text(), end='')
        call_dividends_action()
