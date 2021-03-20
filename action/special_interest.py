"""
Containing the fields, methods and algorithm pertaining to making a decision as to where to place special interests.

As is: It's purely based on the company current train lines, decided by the human players.
To be: Use data to decide where to place special interest cubes.
"""

import util.global_vars as global_vars
import util.output_text as output
from util.constants import *


def special_interest_action():
    print(output.special_interest_action_text())
    global_vars.last_action = ACTION_SPECIAL_INTEREST
    # TODO: alternative, place tracks
