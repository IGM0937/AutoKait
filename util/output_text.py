"""
Program Name:   AutoKait
Description:    The automa A.I. player designed to be used for the board game, Irish Gauge.
Author:         Igor Goran Mačukat
Filename:       output_text.py

Copyright (C) 2021

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not,
see <https://www.gnu.org/licenses/>.

----

Module used to contain all output text to console.
"""

import util.constants as constants


def welcome_text():
    res = "\n"
    res += "Welcome to AutoKait."
    res += "\n"
    res += "Let's play Irish Gauge!"
    res += "\n"
    res += "Please setup the game and proceed when completed..."
    res += "\n"
    return res


def setup_starting_trains_placed(in_dev_mode=False):
    return f"Starting company trains have been placed{str(' in DEV MODE' if in_dev_mode else '')}.\n"


def setup_si_question_prefix():
    return "Which special interest cube is being placed in"


def setup_si_back_function_none_text():
    return invalid_input("back function does not work here. Either 'exit' or continue.")


def setup_si_completed_text(in_dev_mode=False):
    return f"Starting special interest cubes have been placed{str(' in DEV MODE' if in_dev_mode else '')}.\n"


def perform_initial_auctions_text():
    return "Perform initial auctions, if not done so.\n"


def user_input_action_help_text():
    res = "\n"
    res += "Type an action that is taking place outside of Kait's turn or simply press enter for Kait to take her turn."
    res += "\n\n"
    res += "You can type the following text for the following actions:"
    res += "\n"
    res += f" - {constants.BIDDING_LNG} or {constants.BIDDING_SRT} : Start the bidding process"
    res += "\n"
    res += f" - {constants.TRACKS_LNG} or {constants.TRACKS_SRT} : Place company trains onto the board"
    res += "\n"
    res += f" - {constants.INTEREST_LNG} or {constants.INTEREST_SRT} : Place special interests onto the board"
    res += "\n"
    res += f" - {constants.DIVIDEND_LNG} or {constants.DIVIDEND_SRT} : Call for company dividends"
    res += "\n\n"
    res += "If you would like to close the application, type 'exit'."
    res += "\n"
    return res


def user_input_help_text():
    return invalid_input("type 'help' for more information...")


def exit_text(forced, msg="Goodbye"):
    return f"Forced exit... {msg}" if forced else msg


def kait_waiting_turn_text():
    return "Type an action or press enter to take Kait's turn... "


def kait_turn_text():
    return "Kait would like to..."


def invalid_input(text="Try again"):
    return f"Invalid input, {text}.\n"


def special_interest_action_text(is_kait_turn=True):
    return (f"{kait_turn_text()} place" if is_kait_turn else "Placing") + " a special interest cube\n"


def special_interest_action_help_text():
    res = "\n"
    res += "Place a special interest cube for the company Kait has the most share value, prioritising companies " \
           "she owns first."
    res += "\n"
    res += "In case of a tie, place for the company Kait owns that has the most trains on the map."
    res += "\n"
    res += "Choose a colour that isn't present on that trainline yet. If there are multiple colours, choose at random."
    res += "\n\n"
    res += "When deciding on which city to place the cube, select from the following list:"
    res += "\n"
    res += " - Towns occupied by 2+ of Kait's trains"
    res += "\n"
    res += " - Towns occupied by 1 of Kait's trains"
    res += "\n"
    res += " - Towns occupied by 2 different player's trains"
    res += "\n\n"
    res += special_interest_cube_selection_help_text()
    res += "\n\n"
    res += tile_locations_help_text()
    res += "\n\n"
    res += back_and_exit_help_text()
    res += "\n"
    return res


def special_interest_action_be_performed_text():
    return "Can Kait place any special interest cubes? Y/N "


def special_interest_cube_placement_text(plural=False):
    return f"Which special interest cube {'are' if plural else 'is'} being placed?" \
           f" {'(space separated)' if plural else ''} "


def special_interest_cubes_unavailable_text(count, si_cube):
    return invalid_input(f"The {str(count)} {si_cube.split('.')[-1]} {'cubes are' if count > 1 else 'cube is'} "
                         f"not available for selection, try again")


def special_interest_cube_location_placement_text():
    return "Enter the tile location for the special interest cube: "


def special_interest_cube_invalid_location_text():
    return invalid_input("the tile location is not a town or city, try again")


def special_interest_cube_already_present_text(cube_text):
    return invalid_input(f"the tile location already has a {cube_text} special interest cube, try again")


def special_interest_cube_successful_placement_text(tile):
    return f"A {tile.special_interest(True)} special interest cube has been placed in {tile.name()}.\n"


def special_interest_cube_invalid_number_text():
    return invalid_input('invalid number of cubes specified, try again')


def special_interest_cube_invalid_cube_selection_text(cube_text):
    return invalid_input(f"'{str(cube_text)}' is an invalid special interest cube, try again")


def place_tracks_action_text(is_kait_turn=True):
    return (f"{kait_turn_text()} place" if is_kait_turn else "Placing") + " rail tracks\n"


def place_tracks_action_can_place_text():
    return "Can Kait place tracks for any company? Y/N "


def place_tracks_action_help_text():
    res = "\n"
    res += "Place trains for the company that Kait owns, but has the least trains on the map."
    res += "\n"
    res += "If tied, place for the company with the biggest combined share value."
    res += "\n\n"
    res += "Build towards the closest Town or City."
    res += "\n"
    res += "If tied, follow the rule: City (with special interest not present on track) -> City -> Town"
    res += "\n\n"
    res += company_selection_help_text()
    res += "\n\n"
    res += tile_locations_help_text()
    res += "\n\n"
    res += back_and_exit_help_text()
    res += "\n"
    return res


def place_tracks_company_trains_select_text():
    return "Which railway company are you placing the trains for? "


def place_tracks_tile_locations_select_text():
    return "Please enter the tile locations for the new train track: (in order, space separated) "


def place_tracks_tile_location_train_already_present_text():
    return invalid_input("one of the locations already contains required trains, try again")


def place_tracks_unable_difficult_terrain_tile_text():
    return invalid_input("one of the locations is difficult terrain containing a train, try again")


def place_tracks_insufficient_trains_available_text():
    return invalid_input("there are not enough company trains to place on these tiles, try again")


def place_tracks_build_costs_exceeded_text(build_cost):
    return invalid_input(f"total build costs: {str(build_cost)} exceeds the maximum cost of 3, try again")


def place_tracks_adjacent_trains_required_text():
    return invalid_input("tiles applied don't have adjacent trains required, try again")


def place_tracks_new_trains_added_text():
    return "New train tracks have been added to the tiles.\n"


def place_tracks_invalid_number_text():
    return invalid_input('invalid number of trains specified, try again')


def place_tracks_duplicate_tiles_present_text():
    return invalid_input("duplicate tile locations present, try again")


def place_tracks_invalid_tile_locations_text():
    return invalid_input("invalid tile locations present, try again")


def call_auction_action_text():
    return f"{kait_turn_text()} Call an auction action\n"


def call_auction_action_help_text():
    res = "\n"
    res += "Perform an auction on a share for a company that currently has the most connections to Towns or Cities."
    res += "\n"
    res += "If tied, pick the share with the lowest face value."
    res += "\n\n"
    res += "If Kait does not have enough money for that share, she performs Call for Dividends instead."
    res += "\n"
    res += "If Kait is in the bidding war, she will determine the maximum bid based on:"
    res += "\n"
    res += "    (minimum company share + d10 dice roll) capped at Kait's overall money available"
    res += "\n\n"
    res += "Kait will raise the bid at random by from £1 to £3 at a time."
    res += "\n"
    res += "She will pass if she is unable to raise the bid or is unable to got bid past the funds of her maximum " \
           "bid for the share."
    res += "\n\n"
    res += back_and_exit_help_text()
    res += "\n"
    return res


def call_auction_action_be_performed_text():
    return "Can Kait auction the specific share? Y/N "


def place_bid_action_text():
    return "Kait is participating in bids\n"


def place_bid_action_help_text():
    res = "\n"
    res += "Participate in bidding by following the instructions."
    res += "\n\n"
    res += "Type 'back' to back out of bidding. If you would like to close the application, type 'exit'."
    res += "\n"
    return res


def ask_company_minimum_share_price():
    return "Please input the minimum share price of the company being actioned... £ "


def ask_current_bid_price():
    return "Please input the current bid price £ "


def kait_bid_bidding_text(bid):
    return f"Kait is bidding £{str(bid)}\n"


def kait_bid_winning_question_text():
    return "Did Kait win the share or is there a new bid? Y/£ "


def kait_bid_won_text(bid, new_total):
    return f"Kait has won the bid at £{str(bid)}, she now has £{str(new_total)} left.\n"


def kait_bid_passing_text():
    return "Kait is passing\n"


def call_dividends_action_text(is_kait_turn=True):
    return f"{(kait_turn_text() + ' ') if is_kait_turn else ''}Call for dividends\n"


def call_dividends_action_help_text():
    res = "\n"
    res += "If it is Kait's turn, in the event where..."
    res += "\n"
    res += " - There are no dividend cubes in the bag with the same colours owned by Kait's companies."
    res += "\n"
    res += " - OR she does not stand to gain any dividends."
    res += "\n"
    res += "... she will place a special interest cube instead. Otherwise proceed with dividends action."
    res += "\n\n"
    res += special_interest_cube_selection_help_text()
    res += "\n\n"
    res += back_and_exit_help_text()
    res += "\n"
    return res


def call_dividends_action_be_performed_text():
    return "Do the dividend cubes exist in the bag or does Kait stand to gain money? Y/N "


def call_dividends_company_results_text(cbsc, wlw, bcd, gsw, mgw):
    res = "\n"
    res += "The company dividends generated are:"
    res += f"\n - CBSC (yellow) received £{cbsc}"
    res += f"\n - WLW (purple) received £{wlw}"
    res += f"\n - BCD (orange) received £{bcd}"
    res += f"\n - GSW (blue) received £{gsw}"
    res += f"\n - MGW (red) received £{mgw}"
    res += "\n"
    return res


def reward_dividends_text():
    return "How much dividends has Kait won? £ "


def kait_wallet_update_text(dividend, new_total):
    return f"Kait has won £{str(dividend)} in dividends, she now has £{str(new_total)}.\n"


def company_selection_help_text():
    res = "If you are being asked for which company you are placing trains for, you can type the following:"
    res += "\n"
    res += f" - {constants.CBSC_ABV} or {constants.CBSC_COLOUR_SRT} or {constants.CBSC_COLOUR_LNG}" \
           f" : Cork, Bandon & South Coast Railway"
    res += "\n"
    res += f" - {constants.WLW_ABV} or {constants.WLW_COLOUR_SRT} or {constants.WLW_COLOUR_LNG}" \
           f" : Waterford, Limerick & Western Railway"
    res += "\n"
    res += f" - {constants.BCD_ABV} or {constants.BCD_COLOUR_SRT} or {constants.BCD_COLOUR_LNG}" \
           f" : Belfast & Country Down Railway"
    res += "\n"
    res += f" - {constants.GSW_ABV} or {constants.GSW_COLOUR_SRT} or {constants.GSW_COLOUR_LNG}" \
           f" : Great Southern & Western Railway"
    res += "\n"
    res += f" - {constants.MGW_ABV} or {constants.MGW_COLOUR_SRT} or {constants.MGW_COLOUR_LNG}" \
           f" : Midland Great Western Railway"
    return res


def special_interest_cube_selection_help_text():
    res = "If you are being asked about which interest cubes are being placed, you can type the following:"
    res += "\n"
    res += f" - {constants.SI_BLACK_SRT} or {constants.SI_BLACK_LNG} : Black Special Interest Cube"
    res += "\n"
    res += f" - {constants.SI_WHITE_SRT} or {constants.SI_WHITE_LNG} : White Special Interest"
    res += "\n"
    res += f" - {constants.SI_PINK_SRT} or {constants.SI_PINK_LNG} : Pink Special Interest"
    return res


def tile_locations_help_text():
    return "If you are being asked about tile locations, use the map cheat sheet provided to enter location labels."


def back_and_exit_help_text():
    return "If you would like to back out, type 'back' and to close the application, type 'exit'."


def game_over_text(kait_balance=0):
    res = "All of the special interest cubes have been used up."
    res += "\n\n"
    res += f"Kait's end game money in her wallet is £{kait_balance}"
    res += "\n\n"
    res += "The game is over."
    res += "\n\n"
    res += "Thank you for playing with Kait."
    res += "\n"
    res += "Goodbye."
    return res
