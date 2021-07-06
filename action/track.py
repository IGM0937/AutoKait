"""
Program Name:   AutoKait
Description:    The automa A.I. player designed to be used for the board game, Irish Gauge.
Author:         Igor Goran Mačukat
Filename:       track.py

Copyright (C) 2021

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not,
see <https://www.gnu.org/licenses/>.

----

Containing the fields, methods and algorithm pertaining to making a decision to which company to place tracks for.

As is: It's purely based on the current company train count and closes towns and cities, decided by the human players.
To be: Use data to decide which company to place tracks for an where.
"""

from util.tools import *
import action.auction as auction


def place_tracks_action(is_kait_turn=True):
    """
    The preamble to the "Place tracks" action.
    The question will be asked if Kait is able to place tracks
    """
    print(output.place_tracks_action_text(is_kait_turn))
    game_vars.current_action = ACTION_PLACE_TRACKS

    if is_kait_turn:
        yes_answer = ask_user_yes_no_prompt(output.place_tracks_action_can_place_text())
        if is_str_back(yes_answer):
            return
        elif yes_answer:
            choose_company_track()
        else:
            auction.call_auction_action()
    else:
        choose_company_track()


def choose_company_track():
    """
    The preamble to the "Place tracks" action.
    A question will be asked about the chosen company to lay track for.
    See tracks_process function.
    """
    track_placement_complete = False
    while not track_placement_complete:
        company_train = ask_user_get_company_train(output.place_tracks_company_trains_select_text())
        track_placement_complete = True if is_str_back(company_train) else tracks_process(company_train)


def tracks_process(company_train):
    """
    Performs the "Place tracks" action.

    The process will ask, with information from the preamble, where the tacks are going to be placed on the board.
    Once the answers have been inputted, the function will perform a variety of validations to insure that the input
    specified by the user is valid. This validation is based on the rules of the game, found in the user manual.
    See inline comments in function for the list of validations.

    Once complete, the game board is updated, ready for the next turn.
    """

    while True:
        tiles = ask_user_get_board_tiles(output.place_tracks_tile_locations_select_text())

        if is_str_back(tiles):
            return False

        # duplicate trains in the same location
        if any(company_train in tile.trains() for tile in tiles):
            print(output.place_tracks_tile_location_train_already_present_text())
            continue

        # invalidate placement for difficult location containing a train
        if any((tile.tile_type() is TILE_DIFF and len(tile.trains()) > 0) for tile in tiles):
            print(output.place_tracks_unable_difficult_terrain_tile_text())
            continue

        # validate if trains are available for placement
        if not pieces_available(company_train, len(tiles)):
            print(output.place_tracks_insufficient_trains_available_text())
            continue

        # validate build costs
        build_cost = 0
        for tile in tiles:
            if tile.tile_type() is TILE_DIFF:
                build_cost += 2
            else:
                if len(tile.trains()) > 0:
                    build_cost += 1.5
                else:
                    build_cost += 1

        if build_cost > 3:
            print(output.place_tracks_build_costs_exceeded_text(build_cost))
            continue

        # validate placement based on adjacent placement of other trains
        invalid_placement = False
        curr_hex_tiles = []
        for tile in tiles:
            adj_train_found = False
            for curr_hex_tile in curr_hex_tiles:
                if curr_hex_tile in tile.adjacent():
                    adj_train_found = True
                    curr_hex_tiles.append(tile)
                    break

            if not adj_train_found:
                for adj_tile in tile.adjacent():
                    if company_train in adj_tile.trains():
                        adj_train_found = True
                        curr_hex_tiles.append(tile)
                        break

            if not adj_train_found:
                print(output.place_tracks_adjacent_trains_required_text())
                invalid_placement = True
                break

        # conclude
        if invalid_placement:
            continue
        else:
            for curr_hex_tile in curr_hex_tiles:
                curr_hex_tile.add_train(company_train)

            print(output.place_tracks_new_trains_added_text())
            return True
