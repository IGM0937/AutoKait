"""
Program Name:   AutoKait
Description:    The automa A.I. player designed to be used for the board game, Irish Gauge.
Author:         Igor Goran Mačukat
Filename:       tools.py

Copyright (C) 2021

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not,
see <https://www.gnu.org/licenses/>.
"""

from random import randint

import util.global_vars as global_vars
import util.output_text as output
from util.constants import *


def roll_dice(dice_max):
    count, lst = 20, []
    for i in range(count):
        lst.append(randint(1, dice_max))
    return lst[randint(0, count - 1)]


def ask_user_yes_no_prompt(text):
    while True:
        answer = input(text)
        if is_str_yes(answer):
            return True
        elif is_str_no(answer):
            return False
        elif is_str_exit(answer):
            print(output.exit_text(True))
            exit()
        elif is_str_explain(answer):
            explain_action()
        else:
            print(output.invalid_input())


def ask_user_number_prompt(text):
    while True:
        answer = input(text)
        if is_str_exit(answer):
            print(output.exit_text(True))
            exit()
        elif is_str_explain(answer):
            explain_action()
        elif is_str_back(answer):
            return BACK
        else:
            try:
                return int(answer)
            except ValueError:
                pass
            print(output.invalid_input())


def ask_user_cait_bid_prompt(text):
    while True:
        answer = input(text)
        if is_str_exit(answer):
            print(output.exit_text(True))
            exit()
        elif is_str_explain(answer):
            explain_action()
        elif is_str_yes(answer):
            return YES_SRT
        elif is_str_back(answer):
            return BACK
        else:
            try:
                return int(answer)
            except ValueError:
                pass
            print(output.invalid_input())


def explain_action():
    action = global_vars.last_action
    if action == ACTION_SPECIAL_INTEREST:
        print(output.special_interest_action_explain_text())
    elif action == ACTION_PLACE_TRACKS:
        print(output.place_tracks_action_explain_text())
    elif action == ACTION_CALL_AUCTION:
        print(output.call_auction_action_explain_text())
    elif action == ACTION_BIDDING:
        print(output.place_bid_action_explain_text())
    elif action == ACTION_CALL_DIVIDENDS:
        print(output.call_dividends_action_explain_text())


def is_str_yes(value):
    return type(value) is str and (value.lower() == YES_SRT or value.lower() == YES_LNG)


def is_str_no(value):
    return type(value) is str and (value.lower() == NO_SRT or value.lower() == NO_LNG)


def is_str_explain(value):
    return type(value) is str and value.lower() == EXPLAIN


def is_str_back(value):
    return type(value) is str and value.lower() == BACK


def is_str_exit(value):
    return type(value) is str and value.lower() == EXIT
