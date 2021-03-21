"""
Containing the fields, methods and algorithm pertaining to making a decision to which company to place tracks for.

As is: It's purely based on the current company train count and closes towns and cities, decided by the human players.
To be: Use data to decide which company to place tracks for an where.
"""

import util.game_vars as game_vars
import util.output_text as output
from util.constants import *


def place_tracks_action():
    print(output.place_tracks_action_text())
    game_vars.last_action = ACTION_PLACE_TRACKS
