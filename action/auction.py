"""
Program Name:   AutoKait
Description:    The automa A.I. player designed to be used for the board game, Irish Gauge.
Author:         Igor Goran Mačukat
Filename:       auction.py

Copyright (C) 2021

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not,
see <https://www.gnu.org/licenses/>.

----

Containing the fields, methods and algorithm pertaining to making a decision to which company to auction for.

As is: It's purely based on the company with most connections, and decided by the human players.
To be: Use data to decide which company to auction for.
"""

from action.bidding import take_bidding_action
from action.dividends import call_dividends_action
from util.game_vars import *
from util.tools import *


def call_auction_action():
    if data_point[PLAYER_KAIT].balance() <= 0:
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
