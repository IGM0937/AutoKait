"""
Containing the fields, methods and algorithm pertaining to making a decision as to where to place special interests.

As is: It's purely based on the company current train lines, decided by the human players.
To be: Use data to decide where to place special interest cubes.
"""

import util.game_vars as game_vars
import util.output_text as output
import util.tools as tools
from action.track import place_tracks_action
from util.constants import *


def special_interest_action():
    print(output.special_interest_action_text())
    game_vars.last_action = ACTION_SPECIAL_INTEREST
    if not tools.ask_user_yes_no_prompt(output.special_interest_action_be_performed_text()):
        place_tracks_action()
