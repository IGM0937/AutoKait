"""
Program Name:   AutoKait
Description:    The automa A.I. player designed to be used for the board game, Irish Gauge.
Author:         Igor Goran Mačukat
Filename:       autokait.py

Copyright (C) 2021

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not,
see <https://www.gnu.org/licenses/>.
"""

import sys

import action.auction as auction
import action.bidding as bidding
import action.dividends as dividends
import action.special_interest as special_interest
import action.track
import action.track as track
from util.game_vars import *


def perform_setup(in_dev_mode=False):
    """
    Performs introductions, player, data and game information setup.

    For development mode, see setup_init_game_pieces() function in util.game_vars.py module.

    As is: Basic Kait player data and game information setup.
    To be: Setup player, data and game information to be used thought the application.
    """
    print(output.welcome_text())
    setup_players()
    setup_tile_board()
    setup_init_game_pieces(in_dev_mode)


def perform_initial_auctions():
    """
    Performs the initial auctions that happen before game starts proper.

    As is: Basic text output stating to perform initial auctions manually.
    To be: Create an interactive setup for the initial auctions.
    """
    print(output.perform_initial_auctions_text())


def make_decision():
    """
    Decision making algorithm.

    As is: Arbitrary d6 dice roll.
    To be: Use data points to calculate what is the best action to take.
    """
    result = tools.roll_dice(6)
    if result in DICE_RANGE_SPECIAL_INTEREST:
        special_interest.special_interest_action(True)
    elif result in DICE_RANGE_PLACE_TRACKS:
        track.place_tracks_action(True)
    elif result in DICE_RANGE_CALL_AUCTION:
        auction.call_auction_action()
    elif result in DICE_RANGE_CALL_DIVIDENDS:
        dividends.call_dividends_action(True)


def start_event_loop():
    """
    The main event loop after every turn of Kait or other players.

    As is: It is simply concerned for Kait's turn, until the end game condition is met.
    To be: Keep track of all player turns, taking in data every turn to use when it's Kait's turn.
    """
    while not tools.end_game_condition_met():
        game_vars.current_action = ACTION_USER_INPUT
        req = input(output.kait_waiting_turn_text()).lower()
        if tools.is_str_exit(req):
            print(output.exit_text(False))
            exit()
        elif tools.is_str_help(req):
            tools.help_action()
        elif req == BIDDING_SRT or req == BIDDING_LNG:
            bidding.take_bidding_action(False)
        elif req == DIVIDEND_SRT or req == DIVIDEND_LNG:
            dividends.call_dividends_action(False)
        elif req == TRACKS_SRT or req == TRACKS_LNG:
            track.place_tracks_action(False)
        elif req == INTEREST_SRT or req == INTEREST_LNG:
            special_interest.special_interest_action(False)
        elif req != BLANK:
            print(output.user_input_help_text())
        else:
            make_decision()


def perform_dismantle():
    """
    Performs processes typically found at the end of the game.

    As is: Simply outputs end of game text.
    To be: Output detailed results showing winner, stats and so on.
    """
    print(output.game_over_text())


if __name__ == '__main__':
    perform_setup(True if '-d' in sys.argv or '--dev' in sys.argv else False)
    perform_initial_auctions()
    start_event_loop()
    perform_dismantle()
