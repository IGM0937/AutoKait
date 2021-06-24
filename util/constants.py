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
HELP = 'help'

# user inputs, actions
BIDDING_SRT = 'bid'
BIDDING_LNG = 'bidding'
TRACKS_SRT = 'trk'
TRACKS_LNG = 'tracks'
INTEREST_SRT = 'int'
INTEREST_LNG = 'interest'
DIVIDEND_SRT = 'div'
DIVIDEND_LNG = 'dividend'

# user inputs, companies
CBSC_ABV = 'cbsc'
CBSC_COLOUR_SRT = 'y'
CBSC_COLOUR_LNG = 'yellow'
WLW_ABV = 'wlw'
WLW_COLOUR_SRT = 'p'
WLW_COLOUR_LNG = 'purple'
BCD_ABV = 'bcd'
BCD_COLOUR_SRT = 'o'
BCD_COLOUR_LNG = 'orange'
GSW_ABV = 'gsw'
GSW_COLOUR_SRT = 'b'
GSW_COLOUR_LNG = 'blue'
MGW_ABV = 'mgw'
MGW_COLOUR_SRT = 'r'
MGW_COLOUR_LNG = 'red'

# user inputs, special interest cubes
SI_BLACK_SRT = 'b'
SI_BLACK_LNG = 'black'
SI_WHITE_SRT = 'w'
SI_WHITE_LNG = 'white'
SI_PINK_SRT = 'p'
SI_PINK_LNG = 'pink'

# actions tags
ACTION_USER_INPUT = 'action.user_input'
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

# company trains
TRAIN_CBSC = 'train.cork.bandon.south.coast.railway'
TRAIN_WLW = 'train.waterford.limerick.western.railway'
TRAIN_BCD = 'train.belfast.country.down.railway'
TRAIN_GSW = 'train.great.southern.western.railway'
TRAIN_MGW = 'train.midland.great.western.railway'

# special interest cubes
CUBE_SI_BLACK = 'cube.special.interest.black'
CUBE_SI_WHITE = 'cube.special.interest.white'
CUBE_SI_PINK = 'cube.special.interest.pink'

# player data point tags
PLAYER_CAIT = 'data.player.cait'

# number of game pieces
pieces_cubes_si_black = 10
pieces_cubes_si_white = 10
pieces_cubes_si_pink = 10
pieces_trains_cbsc = 19
pieces_trains_wlw = 19
pieces_trains_bcd = 19
pieces_trains_gsw = 19
pieces_trains_mgw = 19

# dice actions range
DICE_RANGE_SPECIAL_INTEREST = range(1, 2)
DICE_RANGE_PLACE_TRACKS = range(2, 5)
DICE_RANGE_CALL_AUCTION = range(5, 6)
DICE_RANGE_CALL_DIVIDENDS = range(6, 7)

# bidding step range and ratio
BID_STEPS = (0, 1, 1, 2, 3)
