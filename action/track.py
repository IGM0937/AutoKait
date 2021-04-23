"""
Containing the fields, methods and algorithm pertaining to making a decision to which company to place tracks for.

As is: It's purely based on the current company train count and closes towns and cities, decided by the human players.
To be: Use data to decide which company to place tracks for an where.
"""

from util.tools import *


def place_tracks_action():
    print(output.place_tracks_action_text())
    game_vars.last_action = ACTION_PLACE_TRACKS
    get_company_train()


def get_company_train():
    track_placement_complete = False
    while not track_placement_complete:
        company_train = ask_user_get_company_train("Which railway company are you placing the trains for? ")
        track_placement_complete = True if is_str_back(company_train) else tracks_process(company_train)


# todo: debug: clean up text, wip
def tracks_process(company_train):
    while True:
        tiles = ask_user_get_board_tiles("Please enter the tile locations for the new train track: (in order) ")

        if is_str_back(tiles):
            return False

        # duplicate trains in the same location
        if any(company_train in tile.trains() for tile in tiles):
            print(output.invalid_input(f"one of the locations already contains required trains, try again."))
            continue

        # invalidate placement for difficult location containing a train
        if any((tile.tile_type() == TILE_DIFF and len(tile.trains()) > 0) for tile in tiles):
            print(output.invalid_input("one of the locations is difficult terrain containing a train, try again."))
            continue

        # validate build costs
        build_cost = 0
        for tile in tiles:
            if tile.tile_type() == TILE_DIFF:
                build_cost += 2
            else:
                if len(tile.trains()) > 0:
                    build_cost += 1.5
                else:
                    build_cost += 1

        if build_cost > 3:
            print(output.invalid_input(f"total build costs: {build_cost} exceeds the maximum cost of 3, try again"))
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
                print(output.invalid_input("tiles applied don't have adjacent trains required, try again"))
                invalid_placement = True
                break

        if invalid_placement:
            continue
        else:
            for curr_hex_tile in curr_hex_tiles:
                curr_hex_tile.add_train(company_train)

            # todo: completed comment required
            return True
