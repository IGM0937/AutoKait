"""
Program Name:   AutoKait
Description:    The automa A.I. player designed to be used for the board game, Irish Gauge.
Author:         Igor Goran Mačukat
Filename:       game_objects.py

Copyright (C) 2021

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not,
see <https://www.gnu.org/licenses/>.

----

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
    """
    Players representation.
    Currently only used for Kait to track her Wallet funds.
    """

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
    """
    Tile representation of a digital in memory game board.
    See setup_tile_board() function in util.game_vars.py module

    Location = Location of the tile on board. Eg. a4, g5, k9
    Tile Type = Type to calculate terrain difficulty. See tile terrain difficulties in util.constants.py module.
    Adjacent = A list of adjacent tiles. Maximum of 6.
    Adjacent Set = Boolean value as a gate keeper from changing game board layout. Set to True post setup.
    Trains = A list of trains on the tile. Placement verified in track_process() function in action.track.py module.
    Name = Name of town, city or major city. None if a simple terrain tile.
    Special Interest = Special interest cube on tile. See special interest cubes in util.constants.py module.
    """

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
        game_vars.tools.pieces_take(train)
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
            game_vars.tools.pieces_take(cube)
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
            return "None" if self.__special_interest is None else self.__special_interest.split('.')[-1]
