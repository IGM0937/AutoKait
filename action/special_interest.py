"""
Program Name:   AutoKait
Description:    The automa A.I. player designed to be used for the board game, Irish Gauge.
Author:         Igor Goran Mačukat
Filename:       special_interest.py

Copyright (C) 2021

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not,
see <https://www.gnu.org/licenses/>.

----

Containing the fields, methods and algorithm pertaining to making a decision as to where to place special interests.

As is: It's purely based on the company current train lines, decided by the human players.
        Contains questions in order to update games global variables.

To be: Use data to decide where to place special interest cubes.
"""

import action.track as track
from util.tools import *


def special_interest_action(is_kait_turn=True):
    """
    The first preamble to the "Special Interest cube" action.
    A question will be asked if Kait is able to place any special interest cubes.
    If the actions is played out of Kait's turn, it will simply proceed to the second preamble.
    If Kait is unable to place a cube, trigger the "Place tracks" action instead, otherwise proceed.
    See place_special_interest_cube function.
    """

    print(output.special_interest_action_text(is_kait_turn))
    game_vars.current_action = ACTION_SPECIAL_INTEREST

    if is_kait_turn:
        yes_answer = ask_user_yes_no_prompt(output.special_interest_action_be_performed_text())
        if is_str_back(yes_answer):
            return
        elif yes_answer:
            choose_special_interest_cube()
        else:
            track.place_tracks_action(is_kait_turn)
    else:
        choose_special_interest_cube()


def choose_special_interest_cube():
    """
    The second preamble to the "Special Interest cube" action.
    A question will be asked about what special interest cube colour is being placed on the board.
    This gives the user an opportunity to back out of the action, otherwise proceed.
    See place_special_interest_cube function.
    """
    cube_placement_complete = False
    while not cube_placement_complete:
        cube = ask_user_get_special_interest_cube(output.special_interest_cube_placement_text())
        if is_str_back(cube):
            cube_placement_complete = True
        else:
            cube = cube[0]
            if not pieces_available(cube):
                print(output.special_interest_cubes_unavailable_text(1, cube))
            else:
                cube_placement_complete = place_special_interest_cube(cube)


def place_special_interest_cube(cube):
    """
    Performs the "Special Interest cube" action
    The process in will ask as to the location of the cube placement.
    If the placement is invalid, it will prompt the user to try again until conditions are satisfied.
    """

    while True:
        tiles = ask_user_get_board_tiles(output.special_interest_cube_location_placement_text(), 1)

        if is_str_back(tiles):
            return False

        tile = tiles[0]

        if tile.name() is None:
            print(output.special_interest_cube_invalid_location_text())
            continue

        if tile.special_interest() is not None:
            print(output.special_interest_cube_already_present_text(tile.special_interest(True)))
            continue

        tile.set_special_interest(cube)
        print(output.special_interest_cube_successful_placement_text(tile))
        return True
