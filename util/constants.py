"""
List of constant variables
"""

# user inputs
BLANK = ''
YES_SRT = 'y'
YES_LNG = 'yes'
NO_SRT = 'n'
NO_LNG = 'no'
EXIT = 'exit'
BACK = 'back'
EXPLAIN = 'explain'
BIDDING_SRT = 'bid'
BIDDING_LNG = 'bidding'
DIVIDEND_SRT = 'div'
DIVIDEND_LNG = 'dividend'

# actions tags
ACTION_SPECIAL_INTEREST = 'action.special_interest'
ACTION_PLACE_TRACKS = 'action.place_tracks'
ACTION_CALL_AUCTION = 'action.call_auction'
ACTION_BIDDING = 'action.bidding'
ACTION_CALL_DIVIDENDS = 'action.call_dividends'

# dice actions range
DICE_RANGE_SPECIAL_INTEREST = range(1, 2)
DICE_RANGE_PLACE_TRACKS = range(2, 5)
DICE_RANGE_CALL_AUCTION = range(5, 6)
DICE_RANGE_CALL_DIVIDENDS = range(6, 7)

# bidding step range and ratio
BID_STEPS = (0, 1, 1, 2, 3)
