"""
Containing the fields, methods and algorithm pertaining to making a decision as to where to place special interests.

As is: It's purely based on the company current train lines, decided by the human players.
To be: Use data to decide where to place special interest cubes.
"""

import action.track as track
from util.tools import *


def special_interest_action(is_cait_turn=True):
    print(output.special_interest_action_text(is_cait_turn))
    game_vars.last_action = ACTION_SPECIAL_INTEREST
    answer = ask_user_yes_no_prompt(output.special_interest_action_be_performed_text())
    choose_special_interest_cube() if answer else track.place_tracks_action()


# TODO: clean up output text
# TODO: run more tests on pieces
def choose_special_interest_cube():
    cube_placement_complete = False
    while not cube_placement_complete:
        cube = ask_user_get_special_interest_cube("Which special interest cube is being placed? ")
        if is_str_back(cube):
            cube_placement_complete = True
        else:
            if pieces_available(cube):
                return place_special_interest_cube(cube)
            else:
                print(output.invalid_input("the selected cube is not available for selection, try again"))
                continue


# TODO: clean up output text
# TODO: run more tests on pieces
def place_special_interest_cube(cube):
    while True:
        tiles = ask_user_get_board_tiles("Enter the tile location for the interest cube: ", 1)

        if is_str_back(tiles):
            return False

        tile = tiles[0]

        if tile.name() is None:
            print(output.invalid_input(f"the tile location is not a town or city, try again"))
            continue

        if tile.special_interest() is not None:
            print(output.invalid_input(f"the tile location already has a {str(tile.special_interest(True))} "
                                       + 'special interest cube, try again'))
            continue

        tile.set_special_interest(cube)
        print(f"A {tile.special_interest(True)} special interest cube has been placed in {tile.name()}.\n")
        return True
