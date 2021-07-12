"""
Program Name:   AutoKait
Description:    The automa A.I. player designed to be used for the board game, Irish Gauge.
Author:         Igor Goran Mačukat
Filename:       bidding.py

Copyright (C) 2021

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not,
see <https://www.gnu.org/licenses/>.

----

Containing the fields, methods and algorithm pertaining to making a decisions during bidding.

As is: There is no logic. It's a simply roll of the d10 dice to be added on minimum value of share.
To be: Use data to decide to choose a bidding maximum, iteration and style.
"""

import util.output_text as output
from util.game_vars import *
from util.tools import ask_user_kait_bid_prompt
from util.tools import ask_user_number_prompt
from util.tools import game_vars
from util.tools import is_str_back
from util.tools import is_str_yes
from util.tools import roll_dice


def take_bidding_action(is_kait_first_bid=False):
    """
    Preamble to the bidding action and process.
    A question will be asked to state the minimum price for the share being auctioned.
    See bidding_process function.
    """
    print(output.place_bid_action_text())
    game_vars.current_action = ACTION_BIDDING
    share_min = ask_user_number_prompt(output.ask_company_minimum_share_price())
    if is_str_back(share_min):
        print(output.kait_bid_passing_text())
    else:
        bidding_process(share_min, is_kait_first_bid)


def get_bidding_max(share_min):
    """
    Calculates the maximum cost Kait will be willing to bid.
    The calculation is made based on the minimum share price of the auction + 1d10 dice roll.
    """
    money_max = data_point[PLAYER_KAIT].balance()
    bid_max = share_min + roll_dice(10)
    return bid_max if bid_max <= money_max else money_max


def calculate_new_bid(current_bid, max_bid):
    """
    Calculates Kait's next bid increment.
    The calculation is made by taking the current bid and randomly choosing an increment from a constant.
    If the next increment is equal to the current bid or exceeds Kait's maximum bid, it returns 0, meaning she passes.
    """
    new_bid = current_bid + BID_STEPS[roll_dice(len(BID_STEPS)) - 1]
    return 0 if (new_bid == current_bid or new_bid > max_bid) else new_bid


def bidding_process(min_price, is_kait_first_bid):
    """
    Performs the bidding action, either taken as part of Kait's 'Call an Auction' action
    or as an out of turn action of another player.

    When it is Kait's turn, it will be asked what is the current bid that Kait has to either beat or skip.

    If Kait skips, the bidding process has ended, and Kait will wait for her next turn.
    If Kait beats the current bid, it will ask for the current bid for Kait to either beat or skip.
    If Kait is the last player standing, Kait will win the share and have the bid cost deducted from her wallet.
    """
    valid_input = start_bidding = True
    max_bid = get_bidding_max(min_price)

    while True:
        if is_kait_first_bid:
            bid = min_price
            break
        else:
            bid = ask_user_number_prompt(output.ask_current_bid_price())

        if is_str_back(bid):
            print(output.kait_bid_passing_text())
            start_bidding = False
            break
        elif bid < min_price:
            print(output.invalid_input())
        else:
            break

    if start_bidding:
        new_bid = None
        while True:
            if valid_input:
                new_bid = calculate_new_bid(bid, max_bid)
                if new_bid == 0:
                    print(output.kait_bid_passing_text())
                    break
                else:
                    print(output.kait_bid_bidding_text(new_bid))

            result = ask_user_kait_bid_prompt(output.kait_bid_winning_question_text())
            if is_str_yes(result):
                kait: Player = data_point[PLAYER_KAIT]
                kait.withdraw(new_bid)
                print(output.kait_bid_won_text(new_bid, kait.balance()))
                break
            elif is_str_back(result):
                print(output.kait_bid_passing_text())
                break
            elif result <= new_bid:
                print(output.invalid_input())
                valid_input = False
            else:
                bid = result
                valid_input = True
