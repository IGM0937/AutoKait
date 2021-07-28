CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
TILE_NONE = "tile.none"
TILE_EASY = "tile.easy"
TILE_DIFF = "tile.diff"
TILE_TOWN = "tile.town"
TILE_CITY = "tile.city"
TILE_MCITY = "tile.city.major"
TILE_SELECT = "tile.selected"
TILE_UNSELECT = "tile.unselected"

TILE_IMAGES = {}
MOUSE_X, MOUSE_Y = None, None


def mouse_update(event):
    global MOUSE_X, MOUSE_Y
    MOUSE_X, MOUSE_Y = event.x, event.y
