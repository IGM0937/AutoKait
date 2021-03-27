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
    __adjacent = []
    __trains = []
    __name = None
    __special_interest = None
    __adjacent_set = False

    def __init__(self, location, tile_type):
        self.__location = location
        self.__tile_type = tile_type

    def init_name(self, name):
        self.__name = name
        return self

    def init_special_interest(self, init_special_interest):
        self.__special_interest = init_special_interest
        return self

    def init_trains(self, *trails):
        self.add_train(trails)
        return self

    def add_train(self, train):
        self.__trains.append(train)

    def location(self):
        return self.__location

    def tile_type(self):
        return self.__tile_type

    def set_adjacent(self, *tiles):
        if self.__adjacent_set:
            raise RuntimeError("Adjacent tiles already set.")
            exit()
        else:
            self.__adjacent.append(tiles)
            self.__adjacent_set = True

    def adjacent(self):
        return self.__adjacent

    def trains(self):
        return self.__trains

    def name(self):
        return self.__name

    def set_special_interest(self, cube):
        self.__special_interest = cube

    def special_interest(self):
        return self.__special_interest
