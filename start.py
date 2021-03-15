from random import randint

import util.constants as const
import util.global_vars as global_vars
import util.output_text as output


def explain_action():
    action = global_vars.last_action
    if action == const.ACTION_SPECIAL_INTEREST:
        print(output.special_interest_action_explain_text())
    elif action == const.ACTION_PLACE_TRACKS:
        print(output.place_tracks_action_explain_text())
    elif action == const.ACTION_CALL_AUCTION:
        print(output.call_auction_action_explain_text())
    elif action == const.ACTION_CALL_DIVIDENDS:
        print(output.call_dividends_action_explain_text())


def special_interest_action():
    print(output.special_interest_action_text())
    global_vars.last_action = const.ACTION_SPECIAL_INTEREST


def place_tracks_action():
    print(output.place_tracks_action_text())
    global_vars.last_action = const.ACTION_PLACE_TRACKS


def call_auction_action():
    print(output.call_auction_action_text())
    global_vars.last_action = const.ACTION_CALL_AUCTION
    if not ask_user_prompt(output.call_auction_action_be_performed_text()):
        call_dividends_action()


def call_dividends_action():
    print(output.call_dividends_action_text())
    global_vars.last_action = const.ACTION_CALL_DIVIDENDS
    if not ask_user_prompt(output.call_dividends_action_be_performed_text()):
        special_interest_action()


def ask_user_prompt(text):
    while True:
        answer = input(text).lower()
        if answer == const.YES_SRT or answer == const.YES_LNG:
            return True
        elif answer == const.NO_SRT or answer == const.NO_LNG:
            return False
        elif answer == const.EXIT:
            print(output.exit_text(True))
            exit()
        elif answer == const.EXPLAIN:
            explain_action()
        else:
            print(output.invalid_input())
            continue


special_interest_act_range = range(1, 2)
place_tracks_act_range = range(2, 5)
call_auction_act_range = range(5, 6)
call_dividends_act_range = range(6, 7)


def roll_dice(dice_max):
    count, lst = 20, []
    for i in range(count):
        lst.append(randint(1, dice_max))
    return lst[randint(0, count - 1)]


def take_turn():
    result = roll_dice(6)
    print(output.cait_turn_text(), end='')

    if result in special_interest_act_range:
        special_interest_action()
    elif result in place_tracks_act_range:
        place_tracks_action()
    elif result in call_auction_act_range:
        call_auction_action()
    elif result in call_dividends_act_range:
        call_dividends_action()


def perform_setup():
    print(output.welcome_text())


def start_event_loop():
    while True:
        current_input = input(output.cait_waiting_turn_text()).lower()
        if current_input == const.EXIT:
            print(output.exit_text(False))
            exit()
        if current_input == const.EXPLAIN:
            explain_action()
        else:
            take_turn()


if __name__ == '__main__':
    perform_setup()
    start_event_loop()
