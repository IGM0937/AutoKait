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

import random

import util.game_vars as game_vars
import util.output_text as output
from util.constants import *


def roll_dice(dice_max):
    """
    Performs a dice roll, returning a result between 1 and dice maximum face value.
    """
    count, lst = 20, []
    for i in range(count):
        lst.append(random.randint(1, dice_max))
    return random.choice(lst)


def pieces_available(piece, count=1):
    """
    Function used for game piece dictionary collection.
    Returns availability for a given type of game piece.
    See setup_init_game_pieces() function in util.game_vars.py module
    """
    return True if (game_vars.game_piece_counters[piece] - count) >= 0 else False


def pieces_take(piece, count=1):
    """
    Function used for game piece dictionary collection.
    Subtracts the count of pieces for a given game piece.
    Typically used in tandem with pieces_available() function in util.tools.py module.
    """
    game_vars.game_piece_counters[piece] -= count


def end_game_condition_met():
    """
    Function used for game piece dictionary collection.
    Returns the amount of special interest cubes available in the game.
    Returned values used to calculate the end game condition.
    """
    return 0 == (game_vars.game_piece_counters[CUBE_SI_BLACK] +
                 game_vars.game_piece_counters[CUBE_SI_WHITE] +
                 game_vars.game_piece_counters[CUBE_SI_PINK])


def ask_user_yes_no_prompt(text):
    """
    Helper function for prompting a user question with an yes or no answer.
    Ability to back out, exit and ask for help.
    """
    while True:
        answer = input(text)
        if is_str_yes(answer):
            return True
        elif is_str_no(answer):
            return False
        elif is_str_back(answer):
            return BACK
        elif is_str_exit(answer):
            print(output.exit_text(True))
            exit()
        elif is_str_help(answer):
            help_action()
        else:
            print(output.invalid_input())


def ask_user_number_prompt(text):
    """
    Helper function for prompting a user question with numerical answer.
    Ability to back out, exit and ask for help.
    """
    while True:
        answer = input(text)
        if is_str_back(answer):
            return BACK
        elif is_str_exit(answer):
            print(output.exit_text(True))
            exit()
        elif is_str_help(answer):
            help_action()
        else:
            try:
                return int(answer)
            except ValueError:
                pass
            print(output.invalid_input())


def ask_user_kait_bid_prompt(text):
    """
    Helper function for prompting a user question specific to Kait bidding.
    Ability to back out, exit and ask for help.
    Returns either a 'yes' variation value or numerical value
    """
    while True:
        answer = input(text)
        if is_str_exit(answer):
            print(output.exit_text(True))
            exit()
        elif is_str_help(answer):
            help_action()
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
    """
    Helper function for prompting a user question specific to company train selection.
    Ability to back out, exit and ask for help.
    Returns in the form, e.g. 'train.waterford.limerick.western.railway'
    See company trains in util.constants.py module
    """
    while True:
        answer = input(text)
        if is_str_back(answer):
            return BACK
        elif is_str_exit(answer):
            print(output.exit_text(True))
            exit()
        elif is_str_help(answer):
            help_action()
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


def ask_user_get_special_interest_cube(text, number_of_cubes=1):
    """
    Helper function for prompting a user question specific to special interest cube selection.
    Ability to select multiple cubes, defaulted to one cube.
    Ability to back out, exit and ask for help.
    Returns in the form, e.g. ['cube.special.interest.black', 'cube.special.interest.white']
    See special interest cubes in util.constants.py module
    """
    while True:
        answer = input(text)
        if is_str_back(answer):
            return BACK
        elif is_str_exit(answer):
            print(output.exit_text(True))
            exit()
        elif is_str_help(answer):
            help_action()
            continue

        cubes = answer.lower().split(' ')
        if len(cubes) is not number_of_cubes:
            print(output.special_interest_cube_invalid_number_text())
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
                print(output.special_interest_cube_invalid_cube_selection_text(cube))
                valid_result = False
                break

        if not valid_result:
            continue

        return result


def ask_user_get_board_tiles(text, max_number_of_tiles=3):
    """
    Helper function for prompting a user question specific to board game tile selection.
    Ability to select between 1 and the maximum number of tiles, defaulted to three tiles.
    Ability to back out, exit and ask for help.
    Returns in the form, e.g. [Tile, Tile]
    See setup_tile_board() function in util.game_vars.py module
    """
    while True:
        answer = input(text)
        if is_str_back(answer):
            return BACK
        elif is_str_exit(answer):
            print(output.exit_text(True))
            exit()
        elif is_str_help(answer):
            help_action()
            continue

        tile_locations = answer.lower().split(' ')
        if len(tile_locations) == 0 or len(tile_locations) >= (max_number_of_tiles + 1):
            print(output.place_tracks_invalid_number_text())
        elif any(tile_locations.count(location) > 1 for location in tile_locations):
            print(output.place_tracks_duplicate_tiles_present_text())
        elif any(location not in game_vars.tile_board.keys() for location in tile_locations):
            print(output.place_tracks_invalid_tile_locations_text())
        else:
            result = []
            for tile_location in tile_locations:
                result.append(game_vars.tile_board[tile_location])
            return result


def help_action():
    """
    Function for outputting help text based on current action.
    """
    if game_vars.current_action is ACTION_USER_INPUT:
        print(output.user_input_action_help_text())
    if game_vars.current_action is ACTION_SPECIAL_INTEREST:
        print(output.special_interest_action_help_text())
    elif game_vars.current_action is ACTION_PLACE_TRACKS:
        print(output.place_tracks_action_help_text())
    elif game_vars.current_action is ACTION_CALL_AUCTION:
        print(output.call_auction_action_help_text())
    elif game_vars.current_action is ACTION_BIDDING:
        print(output.place_bid_action_help_text())
    elif game_vars.current_action is ACTION_CALL_DIVIDENDS:
        print(output.call_dividends_action_help_text())


def is_str_yes(value):
    return is_str(value) and (value.lower() == YES_SRT or value.lower() == YES_LNG)


def is_str_no(value):
    return is_str(value) and (value.lower() == NO_SRT or value.lower() == NO_LNG)


def is_str_help(value):
    return is_str(value) and value.lower() == HELP


def is_str_back(value):
    return is_str(value) and value.lower() == BACK


def is_str_exit(value):
    return is_str(value) and value.lower() == EXIT


def is_str_company(value, abv, srt, lng):
    return is_str(value) and (value.lower() == abv or value.lower() == srt or value.lower() == lng)


def is_str_special_interest(value, srt, lng):
    return is_str(value) and (value.lower() == srt or value.lower() == lng)


def is_str(value):
    return type(value) is str
