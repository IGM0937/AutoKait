CANVAS_WIDTH = 720
CANVAS_HEIGHT = 500
CANVAS_X_START = 0
CANVAS_Y_START = 10
CANVAS_X_STEP = 66
CANVAS_Y_STEP = 41
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

ROW_INDEX = {
    'a': 1,
    'b': 3,
    'c': 5,
    'd': 7,
    'e': 9,
    'f': 11,
    'g': 13,
    'h': 15,
    'i': 17,
    'j': 19,
    'k': 21,
    'l': 23,
    'm': 25,
    'n': 27,
    'o': 29,
    'p': 31
}


def on_mouse_update(event):
    # https://stackoverflow.com/questions/11305962/python-tkinter-how-to-get-coordinates-on-scrollable-canvas
    global MOUSE_X, MOUSE_Y
    MOUSE_X = event.widget.canvasx(event.x)
    MOUSE_Y = event.widget.canvasy(event.y)
    # event.widget.find_closest(MOUSE_X, MOUSE_Y)
