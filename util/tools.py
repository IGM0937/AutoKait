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
        answer = input(text).lower()
        if answer == YES_SRT or answer == YES_LNG:
            return True
        elif answer == NO_SRT or answer == NO_LNG:
            return False
        elif answer == EXIT:
            print(output.exit_text(True))
            exit()
        elif answer == EXPLAIN:
            explain_action()
        else:
            print(output.invalid_input())


def ask_user_number_prompt(text):
    while True:
        answer = input(text)
        if answer == EXIT:
            print(output.exit_text(True))
            exit()
        elif answer == EXPLAIN:
            explain_action()
        else:
            try:
                return int(answer)
            except ValueError:
                pass
            print(output.invalid_input())


def ask_user_cait_bid_prompt(text):
    while True:
        answer = input(text)
        if answer == EXIT:
            print(output.exit_text(True))
            exit()
        elif answer == EXPLAIN:
            explain_action()
        elif answer == YES_SRT or answer == YES_LNG:
            return True
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
    elif action == ACTION_CALL_DIVIDENDS:
        print(output.call_dividends_action_explain_text())
