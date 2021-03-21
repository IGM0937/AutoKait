import action.auction as auction
import action.bidding as bidding
import action.dividends as dividends
import action.special_interest as special_interest
import action.track as track
import util.output_text as output
import util.tools as tools
from util.constants import *
from util.game_vars import *


def make_decision():
    """
    Decision making algorithm.

    As is: Arbitrary d6 dice roll.
    To be: Use data points to calculate what is the best action to take.
    """
    result = tools.roll_dice(6)
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
    """
    while True:
        req = input(output.cait_waiting_turn_text()).lower()
        if tools.is_str_exit(req):
            print(output.exit_text(False))
            exit()
        elif tools.is_str_explain(req):
            tools.explain_action()
        elif req == BIDDING_SRT or req == BIDDING_LNG:
            bidding.take_bidding_action(False)
        elif req == DIVIDEND_SRT or req == DIVIDEND_LNG:
            dividends.dividends_process()
        elif req != BLANK:
            print(output.invalid_input())
        else:
            make_decision()


def perform_setup():
    """
    Performs introductions, player, data and game information setup.

    As is: Basic Cait player data and game information setup.
    To be: Setup player, data and game information to be used thought the application.
    """
    data_point[CAIT_WALLET] = 20
    print(output.welcome_text())


if __name__ == '__main__':
    perform_setup()
    start_event_loop()
