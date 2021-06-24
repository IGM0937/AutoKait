"""
Containing the fields, methods and algorithm pertaining to making a decision as to where to place special interests.

As is: It's purely based on the company current train lines, decided by the human players.
To be: Use data to decide where to place special interest cubes.
"""

import action.track as track
from util.tools import *


def special_interest_action(is_kait_turn=True):
    print(output.special_interest_action_text(is_kait_turn))
    game_vars.last_action = ACTION_SPECIAL_INTEREST

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
