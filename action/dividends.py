"""
Program Name:   AutoKait
Description:    The automa A.I. player designed to be used for the board game, Irish Gauge.
Author:         Igor Goran Mačukat
Filename:       dividends.py

Copyright (C) 2021

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not,
see <https://www.gnu.org/licenses/>.

----

Containing the fields, methods pertaining to performing call for dividends.

As is: There is no logic to performing of the dividends.
To be: Most of the decision to choose dividends happens prior to taking action in the main decision algorithm.
"""

from action.special_interest import special_interest_action
from util.global_vars import *
from util.tools import *


def call_dividends_action():
    print(output.call_dividends_action_text())
    global_vars.last_action = ACTION_CALL_DIVIDENDS
    if ask_user_yes_no_prompt(output.call_dividends_action_be_performed_text()):
        dividends_process()
    else:
        print(output.cait_turn_text(), end='')
        special_interest_action()


def dividends_process():
    dividend = ask_user_number_prompt(output.reward_dividends_text())
    if not is_str_back(dividend):
        data_points[CAIT_WALLET] += dividend
        print(output.cait_wallet_update_text(dividend, data_points[CAIT_WALLET]))
