"""
Containing the fields, methods and algorithm pertaining to making a decision to which company to place tracks for.

As is: It's purely based on the current company train count and closes towns and cities, decided by the human players.
To be: Use data to decide which company to place tracks for an where.
"""

from util.tools import *


def place_tracks_action(is_cait_turn=True):
    print(output.place_tracks_action_text(is_cait_turn))
    game_vars.last_action = ACTION_PLACE_TRACKS

    track_placement_complete = False
    while not track_placement_complete:
        company_train = ask_user_get_company_train(output.place_tracks_company_trains_select_text())
        track_placement_complete = True if is_str_back(company_train) else tracks_process(company_train)


def tracks_process(company_train):
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
            print(output.place_tracks_build_costs_exceeded_text())
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
