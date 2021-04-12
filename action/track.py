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
    tracks_process()


# todo: debug: clean up, wip
def tracks_process():
    # todo: use abbreviation of colour, has to match company trains variable
    # todo: use tools, company train/company picker tool?
    company_train_input = input("Which railway company are you placing the trains for? ")
    if company_train_input == 'y':
        company_train = TRAIN_CBSC
    elif company_train_input == 'p':
        company_train = TRAIN_WLW
    elif company_train_input == 'o':
        company_train = TRAIN_BCD
    elif company_train_input == 'b':
        company_train = TRAIN_GSW
    elif company_train_input == 'r':
        company_train = TRAIN_MGW
    else:
        # todo: add error, retry
        print("invalid company input")
        return
    del company_train_input

    track_placement_complete = False
    while not track_placement_complete:
        # todo: use tools, hex tile picker tool?, returns tiles directly?
        # todo: exclude duplicates, invalid hex range, grayed out, etc...
        hex_tiles_string = input("Please enter the tile locations for the new train track: (in order) ")
        hex_tiles = hex_tiles_string.split(' ')
        del hex_tiles_string

        curr_hex_tiles = []
        build_cost = 0
        invalid_placement = False

        # todo: instead of using 'invalid_placement', try to perform validation checks:
        #       of duplicate trains in the same placement
        #       of build costs
        #   before checking adjacent tile placements, for easier code organisation

        for hex_tile in hex_tiles:
            tile = game_vars.tile_board[hex_tile]
            # todo: add error, if tile does not exist, or not needed because of hex tile picker tool?

            if company_train in tile.trains():
                # todo: add error, do retry
                print("invalid, can't add this company train, already exists")
                invalid_placement = True
                break

            adj_train_found = False
            for curr_hex_tile in curr_hex_tiles:
                if curr_hex_tile in tile.adjacent():
                    adj_train_found = True
                    break
            if not adj_train_found:
                for adj_tile in tile.adjacent():
                    if company_train in adj_tile.trains():
                        adj_train_found = True
                        break

            if adj_train_found:
                curr_hex_tiles.append(tile)
                if TILE_DIFF == tile.tile_type():
                    if len(tile.trains()) > 0:
                        # todo: add error, do retry
                        print("invalid, can't add train on diff terrain. blocked by another train")
                        invalid_placement = True
                        break
                    else:
                        build_cost += 2
                else:
                    if len(tile.trains()) > 0:
                        build_cost += 1.5
                    else:
                        build_cost += 1
            else:
                # todo: error exit
                print("invalid, tiles applied don't have adjacent trains required. try again")
                invalid_placement = True
                break

        # see invalid_placement todo comment
        if invalid_placement:
            continue
        else:
            if build_cost > 3:
                print("unable to build tracks, try again: build cost =", build_cost)
            else:
                for curr_hex_tile in curr_hex_tiles:
                    curr_hex_tile.add_train(company_train)
                track_placement_complete = True
