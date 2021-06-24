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
from util.tools import *


def call_auction_action():
    print(output.call_auction_action_text())
    global_vars.last_action = ACTION_CALL_AUCTION
    # TODO: Is there a way to determine if an action can be performed without asking the question?
    # TODO: using the wallet to determine auctions
    if ask_user_yes_no_prompt(output.call_auction_action_be_performed_text()):
        take_bidding_action(True)
    else:
        print(output.cait_turn_text(), end='')
        call_dividends_action()
