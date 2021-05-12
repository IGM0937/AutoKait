"""
Collection of game pieces and objects definitions

POTENTIAL FUTURE VARIABLES:
        - Player
            - Name
            - Wallet/Money
        - Company
            - # of tracks used
            - # of tracks available
            - ordered list of shares and their values
            - # of connections to towns
            - # of connections to cities
            - # of connections to major cities
        - Interest Cube (Manager)
            - # of cubes on map
            - # of cubes used as dividends
            - # of cubes left to be used
            - cube percentage breakdowns
        - Dividend Payout Object (Manager)
            - Dividend history
                - Company payouts?
                - Player payouts?
        - Locations
            - Type: Town, City, Major City
            - Interest Cube type: Black, Pink, White, None
        - Terrain
            - Type: Easy, Medium (Easy + Tracks), Hard (Difficult)
"""
import util.game_vars as game_vars
from util.constants import CUBE_SI_BLACK
from util.constants import CUBE_SI_PINK
from util.constants import CUBE_SI_WHITE
from util.constants import TILE_CITY
from util.constants import TRAIN_BCD
from util.constants import TRAIN_CBSC
from util.constants import TRAIN_GSW
from util.constants import TRAIN_MGW
from util.constants import TRAIN_WLW


class Player:
    def __init__(self, name):
        self.__name = name
        self.__money = 20

    def name(self):
        return self.__name

    def balance(self):
        return self.__money

    def deposit(self, amount):
        self.__money += amount

    def withdraw(self, amount):
        self.__money -= amount


class Tile:
    __location = None
    __tile_type = None
    __adjacent = None
    __trains = None
    __name = None
    __special_interest = None
    __adjacent_set = False

    def __init__(self, *args):
        """
        :argument [0]: Location of the tile. Eg. a1, h4, etc...
        :argument [1]: Tile Type. Tile terrain difficulties in Constants.
        :argument [2]: Name. For named locations such as town or a city.
        """
        if len(args) < 2 or len(args) > 3:
            raise RuntimeError(f"Invalid number of args for {self.__class__.__name__}")
        self.__location = args[0]
        self.__tile_type = args[1]
        if len(args) == 3:
            self.__name = args[2]
        self.__trains = []
        self.__adjacent = ()

    def add_train(self, train):
        self.__trains.append(train)
        if train is TRAIN_CBSC:
            game_vars.tile_trains_cbsc.append(self)
        elif train is TRAIN_WLW:
            game_vars.tile_trains_wlw.append(self)
        elif train is TRAIN_BCD:
            game_vars.tile_trains_bcd.append(self)
        elif train is TRAIN_GSW:
            game_vars.tile_trains_gsw.append(self)
        elif train is TRAIN_MGW:
            game_vars.tile_trains_mgw.append(self)
        else:
            raise RuntimeError(f"Train '{train}' cannot find appropriate list to reference.")

    def location(self):
        return self.__location

    def tile_type(self):
        return self.__tile_type

    def set_adjacent(self, *tiles):
        if self.__adjacent_set:
            raise RuntimeError('Adjacent tiles already set.')
        else:
            self.__adjacent = self.adjacent() + tiles
            self.__adjacent_set = True

    def adjacent(self):
        return self.__adjacent

    def trains(self):
        return self.__trains

    def name(self):
        return self.__name

    def set_special_interest(self, cube):
        if cube is not CUBE_SI_BLACK and cube is not CUBE_SI_WHITE and cube is not CUBE_SI_PINK:
            raise RuntimeError('Special interest cube specified is invalid')
        if self.__name is None:
            raise RuntimeError('Special interest cube cannot be set against an unnamed location.')
        if self.__special_interest is None:
            self.__special_interest = cube
            if cube is CUBE_SI_BLACK:
                game_vars.tile_black_si_cubes.append(self)
            elif cube is CUBE_SI_WHITE:
                game_vars.tile_white_si_cubes.append(self)
            elif cube is CUBE_SI_PINK:
                game_vars.tile_pink_si_cubes.append(self)
            else:
                raise RuntimeError('Special interest cube cannot find appropriate list to reference.')
            self.__tile_type = TILE_CITY
        else:
            raise RuntimeError('Special interest cube already exists:',
                               self.__special_interest,
                               'at',
                               self.__special_interest)

    def special_interest(self, translate=False):
        if not translate:
            return self.__special_interest
        else:
            if self.__special_interest is None:
                return "None"
            elif self.__special_interest is CUBE_SI_BLACK:
                return "black"
            elif self.__special_interest is CUBE_SI_WHITE:
                return "white"
            elif self.__special_interest is CUBE_SI_PINK:
                return "pink"
