"""
Containing the fields, methods pertaining to performing call for dividends.

As is: There is no logic to performing of the dividends.
To be: Most of the decision to choose dividends happens prior to taking action in the main decision algorithm.
"""

from action.special_interest import special_interest_action
from util.tools import *


def call_dividends_action():
    print(output.call_dividends_action_text())
    global_vars.last_action = ACTION_CALL_DIVIDENDS
    if not ask_user_yes_no_prompt(output.call_dividends_action_be_performed_text()):
        special_interest_action()
