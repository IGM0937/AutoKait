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


def dividends_process():
    si_cubes = ask_user_get_special_interest_cube("Which special interest cube are being placed? ", 3)

    if is_str_back(si_cubes):
        return

    # remove duplicates using dictionary creation from keys, back into list again
    si_cubes = list(dict.fromkeys(si_cubes))
    print(str(si_cubes))

    # todo: debug
    cbsc_named_tiles = filter_tile_named_locations_by_train(TRAIN_CBSC)
    wlw_named_tiles = filter_tile_named_locations_by_train(TRAIN_WLW)
    bcd_named_tiles = filter_tile_named_locations_by_train(TRAIN_BCD)
    gsw_named_tiles = filter_tile_named_locations_by_train(TRAIN_GSW)
    mgw_named_tiles = filter_tile_named_locations_by_train(TRAIN_MGW)

    print(str(mgw_named_tiles))

    # dividend = ask_user_number_prompt(output.reward_dividends_text())
    # if not is_str_back(dividend):
    #     cait: Player = data_point[PLAYER_CAIT]
    #     cait.deposit(dividend)
    #     print(output.cait_wallet_update_text(dividend, cait.balance()))


def filter_tile_named_locations_by_train(train):
    return [tile for tile in game_vars.tile_named_locations if lambda_company_named_tiles(tile, train)]


def lambda_company_named_tiles(tile, train): return train in tile.trains()


def lambda_si_tiles(tile, cubes): return tile.special_interest() is not None and tile.special_interest() in cubes
