"""
Containing the fields, methods and algorithm pertaining to making a decision to which company to auction for.

As is: It's purely based on the company with most connections, and decided by the human players.
To be: Use data to decide which company to auction for.
"""

from action.bidding import take_bidding_action
from action.dividends import call_dividends_action
from util.game_vars import *
from util.tools import *


def call_auction_action():
    if data_point[PLAYER_CAIT].balance() <= 0:
        call_dividends_action()
        return

    print(output.call_auction_action_text())
    game_vars.last_action = ACTION_CALL_AUCTION

    yes_answer = ask_user_yes_no_prompt(output.call_auction_action_be_performed_text())
    if is_str_back(yes_answer):
        return
    elif yes_answer:
        take_bidding_action(True)
    else:
        call_dividends_action(True)
