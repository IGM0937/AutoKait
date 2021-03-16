import action.auction as auction
import action.dividends as dividends
import action.special_interest as special_interest
import action.track as track
import util.output_text as output
import util.tools as tools
from util.constants import *


def make_decision():
    """
    Decision making algorithm.

    As is: Arbitrary d6 dice roll.
    To be: Use data to calculate what is the best action to take.
    """
    result = tools.roll_dice(6)
    print(output.cait_turn_text(), end='')

    if result in DICE_RANGE_SPECIAL_INTEREST:
        special_interest.special_interest_action()
    elif result in DICE_RANGE_PLACE_TRACKS:
        track.place_tracks_action()
    elif result in DICE_RANGE_CALL_AUCTION:
        auction.call_auction_action()
    elif result in DICE_RANGE_CALL_DIVIDENDS:
        dividends.call_dividends_action()


def start_event_loop():
    """
    The main event loop after every turn of Cait or other players.

    As is: It is simply concerned for Cait's turn.
    To be: Keep track of all player turns, taking in data every turn to use when it's Cait's turn.

    TODO: allow for Cait to enter out of turn budding manually
    """
    while True:
        current_input = input(output.cait_waiting_turn_text()).lower()
        if current_input == EXIT:
            print(output.exit_text(False))
            exit()
        if current_input == EXPLAIN:
            tools.explain_action()
        else:
            make_decision()


def perform_setup():
    """
    Performs introduction the player, data and game information setup

    As is: No player, data or game information setup performed. It only performs introduction.
    To be: Setup player, data and game information to be used thought the application.
    """
    print(output.welcome_text())


if __name__ == '__main__':
    perform_setup()
    start_event_loop()
