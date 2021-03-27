"""
List of global game variables and their starting defaults, if relevant.
    POTENTIAL FUTURE DATA POINTS:
        * storing the variables in game_objects
        - company rating
        - interest cube rating
        - player threat rating
"""
from util.constants import *
from util.game_objects import *

last_action = None
data_point = {}
tile = {}

# data point tags
PLAYER_CAIT = 'data.player.cait'


# TODO: debug, remove when done
def setup_board():
    tile1 = Tile("A1", TILE_EASY)
    print(f"Test1 {tile1.location()}")
    print(f"Test1 {tile1.name()}")

    tile2 = Tile("A2", TILE_DIFF).init_name("QWE")
    print(f"Test2 {tile2.location()}")
    print(f"Test2 {tile2.name()}")


# TODO: debug, remove when done
if __name__ == '__main__':
    setup_board()
