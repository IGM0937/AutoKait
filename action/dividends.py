"""
Containing the fields, methods pertaining to performing call for dividends.

As is: There is no logic to performing of the dividends.
To be: Most of the decision to choose dividends happens prior to taking action in the main decision algorithm.
"""

from action.special_interest import special_interest_action
from util.tools import *


def call_dividends_action():
    print(output.call_dividends_action_text())
    game_vars.last_action = ACTION_CALL_DIVIDENDS
    yes_answer = ask_user_yes_no_prompt(output.call_dividends_action_be_performed_text())
    dividends_process() if yes_answer else special_interest_action()


# TODO: clean up output text
# TODO: run more tests
def dividends_process():
    si_cubes = ask_user_get_special_interest_cube("Which special interest cube are being placed? ", 3)

    if is_str_back(si_cubes):
        return

    print("\nThe company dividends generated are: ")
    cbsc_dividends = calculate_company_dividends_by_train(TRAIN_CBSC, si_cubes)
    print(f"CBSC (yellow) received £{cbsc_dividends}")
    wlw_dividends = calculate_company_dividends_by_train(TRAIN_WLW, si_cubes)
    print(f"WLW (purple) received £{wlw_dividends}")
    bcd_dividends = calculate_company_dividends_by_train(TRAIN_BCD, si_cubes)
    print(f"BCD (orange) received £{bcd_dividends}")
    gsw_dividends = calculate_company_dividends_by_train(TRAIN_GSW, si_cubes)
    print(f"GSW (blue) received £{gsw_dividends}")
    mgw_dividends = calculate_company_dividends_by_train(TRAIN_MGW, si_cubes)
    print(f"MGW (red) received £{mgw_dividends}\n")

    dividend = ask_user_number_prompt(output.reward_dividends_text())
    if not is_str_back(dividend):
        cait = game_vars.data_point[PLAYER_CAIT]
        cait.deposit(dividend)
        print(output.cait_wallet_update_text(dividend, cait.balance()))


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
