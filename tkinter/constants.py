APP_WIDTH = 850
APP_HEIGHT = 500
CANVAS_WIDTH = 850
CANVAS_HEIGHT = 1380
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
LOCATION_MAP = {}
MOUSE_X, MOUSE_Y = None, None
DRAG_ACTIVE = False

ROW_ALPHA_INDEX = {
    'a': 1, 'b': 3, 'c': 5, 'd': 7, 'e': 9, 'f': 11, 'g': 13, 'h': 15,
    'i': 17, 'j': 19, 'k': 21, 'l': 23, 'm': 25, 'n': 27, 'o': 29, 'p': 31
}
ROW_NUMBER_INDEX = {
    1: 'a', 3: 'b', 5: 'c', 7: 'd', 9: 'e', 11: 'f', 13: 'g', 15: 'h',
    17: 'i', 19: 'j', 21: 'k', 23: 'l', 25: 'm', 27: 'n', 29: 'o', 31: 'p'
}


def convert_row(value):
    return ROW_NUMBER_INDEX.get(value) if type(value) is int else ROW_ALPHA_INDEX.get(value)


def convert_location(location):
    if type(location) is str:
        row = convert_row(location[0])
        column = int(location[1:])
        return None if row is None else (row, column)
    else:
        row = convert_row(location[0])
        column = str(location[1])
        return None if row is None else row + column


def calculate_xy_location(numeric_location):
    row, column = numeric_location
    pos_x = CANVAS_X_START + (CANVAS_X_STEP * column)
    pos_y = CANVAS_Y_START + (CANVAS_Y_STEP * (row + (column % 2)))
    return pos_x, pos_y


def on_mouse_update(event):
    # https://stackoverflow.com/questions/11305962/python-tkinter-how-to-get-coordinates-on-scrollable-canvas
    global MOUSE_X, MOUSE_Y, DRAG_ACTIVE

    if DRAG_ACTIVE:
        pass

    MOUSE_X = event.widget.canvasx(event.x)
    MOUSE_Y = event.widget.canvasy(event.y)


def on_mouse_drag_press(event):
    global DRAG_ACTIVE
    DRAG_ACTIVE = True


def on_mouse_drag_release(event):
    global DRAG_ACTIVE
    DRAG_ACTIVE = False


def on_mouse_vertical_update(event):
    event.widget.yview_scroll(-1 * int(event.delta/50), 'units')


def on_mouse_horizontal_update(event):
    event.widget.xview_scroll(-1 * int(event.delta/50), 'units')
