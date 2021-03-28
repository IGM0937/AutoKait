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

# tile terrain difficulties
TILE_EASY = 'tile.terrain.easy'
TILE_DIFF = 'tile.terrain.difficult'
TILE_TOWN = 'tile.terrain.town'
TILE_CITY = 'tile.terrain.city'
TILE_MCITY = 'tile.terrain.major.city'

# companies
RAILWAY_CBSC = 'company.cork.bandon.south.coast.railway'
RAILWAY_WLW = 'company.waterford.limerick.western.railway'
RAILWAY_BCD = 'company.belfast.country.down.railway'
RAILWAY_GSW = 'company.great.southern.western.railway'
RAILWAY_MGW = 'company.midland.great.western.railway'

# special interest cubes
SI_BLACK = 'special.interest.cube.black'
SI_WHITE = 'special.interest.cube.white'
SI_PINK = 'special.interest.cube.pink'

# player data point tags
PLAYER_CAIT = 'data.player.cait'

# dice actions range
DICE_RANGE_SPECIAL_INTEREST = range(1, 2)
DICE_RANGE_PLACE_TRACKS = range(2, 5)
DICE_RANGE_CALL_AUCTION = range(5, 6)
DICE_RANGE_CALL_DIVIDENDS = range(6, 7)

# bidding step range and ratio
BID_STEPS = (0, 1, 1, 2, 3)
