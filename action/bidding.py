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
from util.constants import *
from util.global_vars import *
from util.tools import ask_user_cait_bid_prompt
from util.tools import ask_user_number_prompt
from util.tools import global_vars
from util.tools import is_str_back
from util.tools import is_str_yes
from util.tools import roll_dice


def take_bidding_action(is_cait_first_bid):
    print(output.place_bid_action_text())
    global_vars.last_action = ACTION_BIDDING
    share_min = ask_user_number_prompt(output.ask_company_minimum_share_price())
    if is_str_back(share_min):
        print(output.cait_bid_passing_text())
    else:
        bidding_process(share_min, is_cait_first_bid)


def get_bidding_max(share_min):
    money_max = data_points[CAIT_WALLET]
    bid_max = share_min + roll_dice(10)
    return bid_max if bid_max <= money_max else money_max


def calculate_caits_bid(current_bid, max_bid):
    new_bid = current_bid + BID_STEPS[roll_dice(len(BID_STEPS)) - 1]
    return 0 if (new_bid == current_bid or new_bid > max_bid) else new_bid


def bidding_process(min_price, is_cait_first_bid):
    valid_input = start_bidding = True
    max_bid = get_bidding_max(min_price)

    while True:
        if is_cait_first_bid:
            bid = min_price
            break
        else:
            bid = ask_user_number_prompt(output.ask_current_bid_price())

        if is_str_back(bid):
            print(output.cait_bid_passing_text())
            start_bidding = False
            break
        elif bid < min_price:
            print(output.invalid_input())
        else:
            break

    if start_bidding:
        while True:
            if valid_input:
                new_bid = calculate_caits_bid(bid, max_bid)
                if new_bid == 0:
                    print(output.cait_bid_passing_text())
                    break
                else:
                    print(output.cait_bid_bidding_text(new_bid))

            result = ask_user_cait_bid_prompt(output.cait_bid_winning_question_text())
            if is_str_yes(result):
                data_points[CAIT_WALLET] -= new_bid
                print(output.cait_bid_won_text(new_bid, data_points[CAIT_WALLET]))
                break
            elif is_str_back(result):
                print(output.cait_bid_passing_text())
                break
            elif result <= new_bid:
                print(output.invalid_input())
                valid_input = False
            else:
                bid = result
                valid_input = True
