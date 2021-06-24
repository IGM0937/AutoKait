"""
Program Name:   AutoKait
Description:    The automa A.I. player designed to be used for the board game, Irish Gauge.
Author:         Igor Goran Mačukat
Filename:       constants.py

Copyright (C) 2021

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not,
see <https://www.gnu.org/licenses/>.

----

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
