"""
Containing the fields, methods and algorithm pertaining to making a decision as to where to place special interests.

As is: It's purely based on the company current train lines, decided by the human players.
To be: Use data to decide where to place special interest cubes.
"""

from action.track import place_tracks_action
from util.tools import *


def special_interest_action():
    print(output.special_interest_action_text())
    game_vars.last_action = ACTION_SPECIAL_INTEREST
    if not ask_user_yes_no_prompt(output.special_interest_action_be_performed_text()):
        place_tracks_action()


# TODO: clean up output text
def choose_special_interest_cube():
    cube_placement_complete = False
    while not cube_placement_complete:
        cube = ask_user_get_special_interest_cube("Which special interest cube are you placing? ")
        cube_placement_complete = True if is_str_back(cube) else place_special_interest_cube(cube)


# TODO: clean up output text
def place_special_interest_cube(cube):
    while True:
        tiles = ask_user_get_board_tiles("Enter the tile location for the interest cube: ", 1)
        tile = tiles[0]

        if is_str_back(tile):
            return False

        if tile.name is None:
            print(output.invalid_input(f"the tile location is not a town or city"))
            continue

        if tile.special_interest() is not None:
            print(output.invalid_input(f"the tile location already has a special interest cube: "
                                       f"{str(tile.special_interest())}"))
            continue

        tile.set_special_interest(cube)
        return True
