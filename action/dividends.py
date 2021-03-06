"""
Program Name:   AutoKait
Description:    The automa A.I. player designed to be used for the board game, Irish Gauge.
Author:         Igor Goran Mačukat
Filename:       dividends.py

Copyright (C) 2021

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not,
see <https://www.gnu.org/licenses/>.

----

Containing the fields, methods pertaining to performing call for dividends.

As is: There is no logic to performing of the dividends.
To be: Most of the decision to choose dividends happens prior to taking action in the main decision algorithm.
"""

from action.special_interest import special_interest_action
from util.tools import *


def call_dividends_action(is_kait_turn=True):
    """
    Preamble to the "Call Dividends" action and process.
    A question will be asked to state if Kait stands to gain any dividends before proceeding.
    If not, trigger the "Special Interest cube" action instead, otherwise proceed.
    See dividends_process function.
    """
    print(output.call_dividends_action_text(is_kait_turn))
    game_vars.current_action = ACTION_CALL_DIVIDENDS

    if is_kait_turn:
        yes_answer = ask_user_yes_no_prompt(output.call_dividends_action_be_performed_text())
        if is_str_back(yes_answer):
            return
        elif yes_answer:
            dividends_process()
        else:
            special_interest_action(is_kait_turn)
    else:
        dividends_process()


def dividends_process():
    """
    Performs the "Call Dividends" action.

    The user will be prompted to draw a maximum of up to 3 cubes and input the colours drawn.
    The process will then calculate the dividends received by each company and output it to the console.
    The user will then be asked to input how much Kait has collected in order for her wallet to be updated.
    Once complete, cubes drawn for the calculations are taken out of the game.
    """
    si_cubes_available = game_vars.game_piece_counters[CUBE_SI_BLACK] + \
                         game_vars.game_piece_counters[CUBE_SI_WHITE] + \
                         game_vars.game_piece_counters[CUBE_SI_PINK]
    si_cubes_select = 3 if si_cubes_available >= 3 else si_cubes_available

    selection_complete = False
    while not selection_complete:
        si_cubes = ask_user_get_special_interest_cube(output.special_interest_cube_placement_text(plural=True),
                                                      si_cubes_select)

        if is_str_back(si_cubes):
            return

        # validate if pieces are available to be selected
        valid_pieces_available = True
        for si_cube in si_cubes:
            si_cubes_count = si_cubes.count(si_cube)
            if not pieces_available(si_cube, si_cubes_count):
                print(output.special_interest_cubes_unavailable_text(si_cubes_count, si_cube))
                valid_pieces_available = False
                break
        if not valid_pieces_available:
            continue

        cbsc_div = calculate_company_dividends_by_train(TRAIN_CBSC, si_cubes)
        wlw_div = calculate_company_dividends_by_train(TRAIN_WLW, si_cubes)
        bcd_div = calculate_company_dividends_by_train(TRAIN_BCD, si_cubes)
        gsw_div = calculate_company_dividends_by_train(TRAIN_GSW, si_cubes)
        mgw_div = calculate_company_dividends_by_train(TRAIN_MGW, si_cubes)

        output.call_dividends_company_results_text(cbsc_div, wlw_div, bcd_div, gsw_div, mgw_div)

        dividend = ask_user_number_prompt(output.reward_dividends_text())
        if not is_str_back(dividend):
            kait = game_vars.data_point[PLAYER_KAIT]
            kait.deposit(dividend)
            print(output.kait_wallet_update_text(dividend, kait.balance()))

            # reduce piece counters and complete
            for si_cube in si_cubes:
                pieces_take(si_cube)
            selection_complete = True


def calculate_company_dividends_by_train(train, si_cubes):
    scoring_tiles = filter_scoring_named_locations_by_company_train(train, si_cubes)
    has_town = any(tile.tile_type() is TILE_TOWN for tile in scoring_tiles)
    paying_cities = [tile for tile in scoring_tiles if
                     tile.tile_type() is TILE_CITY or tile.tile_type() is TILE_MCITY]

    total_dividends = 0
    if (has_town and len(paying_cities) > 0) or len(paying_cities) > 1:
        for tile in scoring_tiles:
            if tile.tile_type() is TILE_TOWN:
                total_dividends += 2
            elif tile.tile_type() is TILE_CITY or tile.tile_type() is TILE_MCITY:
                total_dividends += 4
    return total_dividends


def filter_scoring_named_locations_by_company_train(train, cubes):
    return [tile for tile in game_vars.tile_named_locations if
            (train in tile.trains()) and (tile.special_interest() is None or tile.special_interest() in cubes)]
