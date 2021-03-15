"""
Containing the fields, methods and algorithm pertaining to making a decision to which company to auction for.

As is: It's purely based on the company with most connections, and decided by the human players.
To be: Use data to decide which company to auction for.
"""
from action import bidding
from action.dividends import call_dividends_action
from util.tools import *


def call_auction_action():
    print(output.call_auction_action_text())
    global_vars.last_action = ACTION_CALL_AUCTION
    if not ask_user_yes_no_prompt(output.call_auction_action_be_performed_text()):
        call_dividends_action()
    else:
        share_min = ask_user_number_prompt(output.ask_company_minimum_share_price())
        cait_bid = bidding.get_bidding_max(share_min)
        input(output.cait_blind_bid_ready())
        print(output.cait_blind_bid_reveal(cait_bid))
