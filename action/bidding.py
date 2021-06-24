"""
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
    print(output.place_bid_action_text())
    game_vars.last_action = ACTION_BIDDING
    share_min = ask_user_number_prompt(output.ask_company_minimum_share_price())
    if is_str_back(share_min):
        print(output.kait_bid_passing_text())
    else:
        bidding_process(share_min, is_kait_first_bid)


def get_bidding_max(share_min):
    money_max = data_point[PLAYER_KAIT].balance()
    bid_max = share_min + roll_dice(10)
    return bid_max if bid_max <= money_max else money_max


def calculate_new_bid(current_bid, max_bid):
    new_bid = current_bid + BID_STEPS[roll_dice(len(BID_STEPS)) - 1]
    return 0 if (new_bid == current_bid or new_bid > max_bid) else new_bid


def bidding_process(min_price, is_kait_first_bid):
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
