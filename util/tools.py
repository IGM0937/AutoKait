import random

import util.game_vars as game_vars
import util.output_text as output
from util.constants import *


def roll_dice(dice_max):
    count, lst = 20, []
    for i in range(count):
        lst.append(random.randint(1, dice_max))
    return random.choice(lst)


def pieces_available(piece, count=1):
    return True if (game_vars.game_piece_counters[piece] - count) >= 0 else False


def pieces_take(piece, count=1):
    game_vars.game_piece_counters[piece] -= count


def end_game_condition_met():
    return 0 >= (game_vars.game_piece_counters[CUBE_SI_BLACK] +
                 game_vars.game_piece_counters[CUBE_SI_WHITE] +
                 game_vars.game_piece_counters[CUBE_SI_PINK])


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


def ask_user_get_company_train(text):
    while True:
        answer = input(text)
        if is_str_exit(answer):
            print(output.exit_text(True))
            exit()
        elif is_str_back(answer):
            return BACK
        elif is_str_explain(answer):
            explain_action()
        elif is_str_company(answer, CBSC_ABV, CBSC_COLOUR_SRT, CBSC_COLOUR_LNG):
            return TRAIN_CBSC
        elif is_str_company(answer, WLW_ABV, WLW_COLOUR_SRT, WLW_COLOUR_LNG):
            return TRAIN_WLW
        elif is_str_company(answer, BCD_ABV, BCD_COLOUR_SRT, BCD_COLOUR_LNG):
            return TRAIN_BCD
        elif is_str_company(answer, GSW_ABV, GSW_COLOUR_SRT, GSW_COLOUR_LNG):
            return TRAIN_GSW
        elif is_str_company(answer, MGW_ABV, MGW_COLOUR_SRT, MGW_COLOUR_LNG):
            return TRAIN_MGW
        else:
            print(output.invalid_input())


def ask_user_get_special_interest_cube(text, number_cubes=1):
    while True:
        answer = input(text)
        if is_str_explain(answer):
            explain_action()
        elif is_str_back(answer):
            return BACK
        elif is_str_exit(answer):
            print(output.exit_text(True))
            exit()

        cubes = answer.lower().split(' ')
        if len(cubes) is not number_cubes:
            print(output.invalid_input('invalid number of cubes specified, try again'))
            continue

        result = []
        valid_result = True
        for cube in cubes:
            if is_str_special_interest(cube, SI_BLACK_SRT, SI_BLACK_LNG):
                result.append(CUBE_SI_BLACK)
            elif is_str_special_interest(cube, SI_WHITE_SRT, SI_WHITE_LNG):
                result.append(CUBE_SI_WHITE)
            elif is_str_special_interest(cube, SI_PINK_SRT, SI_PINK_LNG):
                result.append(CUBE_SI_PINK)
            else:
                print(output.invalid_input(f"'{str(cube)}' is an invalid special interest cube, try again"))
                valid_result = False
                break

        if not valid_result:
            continue

        return result


def ask_user_get_board_tiles(text, max_tiles=3):
    while True:
        answer = input(text)
        if is_str_back(answer):
            return BACK
        elif is_str_exit(answer):
            print(output.exit_text(True))
            exit()

        tile_locations = answer.lower().split(' ')
        if len(tile_locations) == 0 or len(tile_locations) >= (max_tiles + 1):
            print(output.invalid_input('invalid number of trains specified, try again'))
        elif any(tile_locations.count(location) > 1 for location in tile_locations):
            print(output.invalid_input("duplicate tile locations present, try again"))
        elif any(location not in game_vars.tile_board.keys() for location in tile_locations):
            print(output.invalid_input("invalid tile locations present, try again"))
        else:
            result = []
            for tile_location in tile_locations:
                result.append(game_vars.tile_board[tile_location])
            return result


def explain_action():
    if game_vars.last_action is ACTION_USER_INPUT:
        print(output.user_input_action_explain_text())
    if game_vars.last_action is ACTION_SPECIAL_INTEREST:
        print(output.special_interest_action_explain_text())
    elif game_vars.last_action is ACTION_PLACE_TRACKS:
        print(output.place_tracks_action_explain_text())
    elif game_vars.last_action is ACTION_CALL_AUCTION:
        print(output.call_auction_action_explain_text())
    elif game_vars.last_action is ACTION_BIDDING:
        print(output.place_bid_action_explain_text())
    elif game_vars.last_action is ACTION_CALL_DIVIDENDS:
        print(output.call_dividends_action_explain_text())


def is_str_yes(value):
    return is_str(value) and (value.lower() is YES_SRT or value.lower() is YES_LNG)


def is_str_no(value):
    return is_str(value) and (value.lower() is NO_SRT or value.lower() is NO_LNG)


def is_str_explain(value):
    return is_str(value) and value.lower() is EXPLAIN


def is_str_help(value):
    return is_str(value) and value.lower() is HELP


def is_str_back(value):
    return is_str(value) and value.lower() is BACK


def is_str_exit(value):
    return is_str(value) and value.lower() is EXIT


def is_str_company(value, abv, srt, lng):
    return is_str(value) and (value.lower() is abv or value.lower() is srt or value.lower() is lng)


def is_str_special_interest(value, srt, lng):
    return is_str(value) and (value.lower() is srt or value.lower() is lng)


def is_str(value):
    return type(value) is str
