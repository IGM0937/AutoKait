"""
Containing the fields, methods pertaining to performing call for dividends.

As is: There is no logic to performing of the dividends.
To be: Most of the decision to choose dividends happens prior to taking action in the main decision algorithm.
"""

from action.special_interest import special_interest_action
from util.game_vars import *
from util.tools import *


def call_dividends_action():
    print(output.call_dividends_action_text())
    game_vars.last_action = ACTION_CALL_DIVIDENDS
    if ask_user_yes_no_prompt(output.call_dividends_action_be_performed_text()):
        dividends_process()
    else:
        special_interest_action()


def dividends_process():
    dividend = ask_user_number_prompt(output.reward_dividends_text())
    if not is_str_back(dividend):
        cait: Player = data_point[PLAYER_CAIT]
        cait.deposit(dividend)
        print(output.cait_wallet_update_text(dividend, cait.balance()))
